# Uv collections

`UvPackage` installs Python distributions and their transitive dependencies into
one Spack prefix. Python, uv, compilers, and native libraries remain Spack
dependencies; distributions resolved by uv do not appear in the Spack DAG.

```python
from spack_repo.builtin.build_systems.uv import UvPackage
from spack.package import *

class MyCollection(UvPackage):
    version("1")
    python_dependencies = {"requests": "2.32.3", "click": None}
    depends_on("python@3.13:", type=("build", "run"))
    # Declare compilers and native libraries needed by this collection here.
```

Use a tuple of distribution names for unpinned roots or a mapping from names to
exact versions (`None` leaves a root unpinned). Names are distribution names,
which can differ from import names. `python_index_url` defaults to PyPI.

The builder uses Spack's `py-uv` executable and selected Python interpreter.
It disables uv configuration discovery, managed interpreters, and Python
downloads. `uv pip compile --generate-hashes` resolves the roots together;
`uv pip sync --require-hashes --prefix` installs into the collection prefix.
Wheels are allowed and source builds use uv's default build isolation. Declare
native build and runtime requirements explicitly. Installed files are copied
from the stage cache. Python scripts refer to the selected Spack interpreter.
As with other Python extensions, loading the collection must expose its
site-packages directory to that interpreter.

`.spack-uv` retains `requirements.in`, hashed `requirements.txt`, `uv-info.txt`,
`verify.py`, and `packages.json`. Verification checks requested distributions
and their exact versions in the collection's own site-packages directories.
It does not infer or import modules from distribution names.

Set `uv_lockfile` to an absolute path or a path relative to `stage.source_path`
(e.g. a checksummed resource) to replay a reviewed hashed requirements file.
This is a requirements.txt lock, not uv's project-format `uv.lock`. Replay
skips resolution, requires hashes, and still checks roots against the recipe.
Locks must match the selected Python version and target platform.

## Prototype limits

Downloads happen during installation, outside Spack's fetch cache, mirrors,
and source staging. A spec hash does not capture an unpinned resolution.
Pin roots and provide a reviewed lockfile for controlled rebuilds. Requirements
hashes cover distribution artifacts; isolated source build dependencies are
resolved separately by uv and are not fully captured in that lockfile.
Downloaded wheels and source builds do not automatically gain Spack relocation
metadata. Validate native linking and runtime imports for each collection on
its target platform. This builder does not migrate existing Python recipes.

See the upstream [compile documentation](https://docs.astral.sh/uv/pip/compile/)
and [CLI reference](https://docs.astral.sh/uv/reference/cli/).
