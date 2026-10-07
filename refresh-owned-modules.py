#!/usr/bin/env python3
import argparse
import json
import os
import shlex
import subprocess
import sys
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("environment")
parser.add_argument("parents", nargs="*")
parser.add_argument("--apply", action="store_true")
args = parser.parse_args()

spack = os.environ.get("SPACK_COMMAND", "spack")


def hashes(environment):
    # Refresh skips upstream installations, so they cannot claim module ownership.
    result = subprocess.run(
        [
            spack,
            "-e",
            environment,
            "find",
            "--install-tree",
            "local",
            "--format",
            "{hash}",
            "--no-groups",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return set(result.stdout.split())


def module_paths(environment, spec_hashes):
    # Ask Spack for the actual layout, including hierarchy, projections and exclusions.
    code = """
import json
import sys
import spack.modules
import spack.repo
import spack.store

paths = {}
for h in json.load(sys.stdin):
    spec = spack.store.STORE.db.query_one('/' + h)
    if spec is None:
        raise RuntimeError('Installed spec disappeared: ' + h)
    if not spack.repo.PATH.exists(spec.name):
        continue
    writer = spack.modules.module_types['lmod'](spec, 'default')
    paths[h] = None if writer.conf.excluded else {
        'path': writer.layout.filename, 'use_name': writer.layout.use_name
    }
print(json.dumps(paths))
"""
    result = subprocess.run(
        [spack, "-e", environment, "python", "-c", "exec(" + repr(code) + ")"],
        input=json.dumps(sorted(spec_hashes)),
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


downstream = hashes(args.environment)
inherited = set()
parent_paths = {}
dependency_owners = {}
for parent in args.parents:
    parent_hashes = hashes(parent)
    for h, module in module_paths(parent, parent_hashes - inherited).items():
        dependency_owners[h] = None if module is None else module['use_name']
        if module is not None:
            parent_paths.setdefault(module['path'], h)
    inherited.update(parent_hashes)

owned = sorted(downstream - inherited)

print(f"Skipping {len(downstream & inherited)} parent-owned specs.")
print(f"Refreshing {len(owned)} candidates before module exclusions.")

# An empty constraint list would refresh the entire environment.
if not owned:
    raise SystemExit(0)

# Different hashes can still name the same module when hash_length is zero.
# Check all candidates together, before batching, so no partial refresh occurs.
claimed_paths = dict(parent_paths)
collisions = []
for h, module in module_paths(args.environment, owned).items():
    if module is None:
        continue
    path = module['path']
    previous = claimed_paths.setdefault(path, h)
    if previous != h:
        collisions.append(f"{path}\n  /{previous}\n  /{h}")
if collisions:
    print("Module path collisions; refresh aborted before writing:\n"
          + "\n".join(collisions)
          + "\nAdd distinct projections or suffixes for these builds.", file=sys.stderr)
    raise SystemExit(1)

# Pass the parent names to each refresh without changing the child's layout.
with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as ownership:
    json.dump(dependency_owners, ownership)
    ownership.flush()
    refresh_env = dict(os.environ, SPACK_LMOD_DEPENDENCY_OWNERS=ownership.name)
    # Batch requests to stay below command-line size limits.
    for start in range(0, len(owned), 100):
        command = [
            spack, "-e", args.environment, "module", "lmod", "refresh", "-y",
            *("/" + h for h in owned[start : start + 100]),
        ]
        if args.apply:
            subprocess.run(command, check=True, env=refresh_env)
        else:
            print(shlex.join(command))
