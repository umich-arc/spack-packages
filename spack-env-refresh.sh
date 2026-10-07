#!/usr/bin/env bash

# The first environment containing a concrete hash owns its modulefile.
# Keep this order: downstream environments must not rewrite parent modules.
set -uo pipefail

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
environments=(arc-core-stacks arc-aocc-stacks r-stacks bioinformatics paraview py-stacks)
if (($# > 1)); then
    printf 'Usage: %s [environment]\n' "$0" >&2
    exit 2
fi
selected=${1-}
if (($# == 1)); then
    found=false
    for environment in "${environments[@]}"; do
        if [[ "$environment" == "$selected" ]]; then
            found=true
            break
        fi
    done
    if [[ "$found" == false ]]; then
        printf 'Unknown environment: %s\nAvailable environments: %s\n' \
            "$selected" "${environments[*]}" >&2
        exit 2
    fi
fi
parents=()
failed=()

for environment in "${environments[@]}"; do
    if [[ -n "$selected" && "$environment" != "$selected" ]]; then
        parents+=("$environment")
        continue
    fi
    echo "Refreshing modules owned by ${environment}"
    if ! python3 "$script_dir/refresh-owned-modules.py" --apply \
        "$environment" "${parents[@]}"; then
        failed+=("$environment")
    fi
    parents+=("$environment")
    if [[ -n "$selected" ]]; then
        break
    fi
done

if ((${#failed[@]})); then
    printf 'Module refresh failed: %s\n' "${failed[@]}" >&2
    exit 1
fi
