# Pak collections

`PakPackage` installs an R collection and its transitive R dependencies into
`<prefix>/rlib/R/library`. R, compilers, and native libraries remain Spack
dependencies. R packages resolved by pak are not represented in the Spack DAG.
The existing `RPackage` and `RCollectivePackage` builders are unaffected.

```python
from spack_repo.builtin.build_systems.pak import PakPackage
from spack.package import *

class MyCollection(PakPackage):
    version("1")
    r_dependencies = {"tidyverse": "2.0.0", "cli": None}
    r_github_dependencies = {"mypackage": "organization/repository@commit"}
    depends_on("r@4.5:", type=("build", "run"))
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    # Declare all native libraries required by this collection here.
```

Use a tuple of names for unpinned roots, or a mapping for exact versions.
`r_repositories` maps repository names to HTTP(S) URLs. `bioc_version` selects
a Bioconductor release. Pak resolves all roots together, including Depends,
Imports, and LinkingTo. Suggested packages are excluded. Source builds and
one installation worker are selected; pak system package installation is disabled.

The builder uses pak already installed in the selected R interpreter's base
library (`.Library`). It checks that pak loads and exports the required lockfile
API, and fails clearly if it does not. It never downloads or installs pak.
The pak version and location are recorded in `.spack-pak/pak-info.txt`.
The target library is passed
explicitly to lockfile installation. Base and recommended packages supplied by
R may satisfy dependencies without being duplicated in the collection.

`.spack-pak` retains `install.R`, `pkg.lock`, `packages.tsv`, and
`session-info.txt` for diagnosis. Installation fails if a requested root is
missing, a pinned version differs, or a root namespace cannot load.

To replay a reviewed resolution, set `pak_lockfile` to an absolute path or a
path relative to `stage.source_path`, such as a staged resource. The lockfile
is copied into the prefix and installed without re-resolving. Its roots and
exact root versions are still checked against the recipe.

## Prototype limits

Collection package downloads occur during installation. They do not
currently use Spack's fetch cache, checksum verification, mirrors, or offline
source staging. This must be addressed before use in a deployment requiring
Spack's source provenance guarantees.

A Spack spec hash does not capture a newly resolved pak graph. Pin root
versions, GitHub commit hashes, and repository snapshots; ship a reviewed
lockfile as a checksummed Spack resource for controlled rebuilds. A generated
lockfile records the resolution, but upstream URLs can disappear; it is not a
permanent source archive. Lockfiles should be created for the target R version
and platform. Pak does not supply Spack relocation metadata for downloaded R
packages. Native library discovery and runtime linking require validation for
each collection on its target platform.

The migrated `rtidyverse` recipe demonstrates the builder and pins tidyverse
2.0.0. Its full online installation needs validation with its declared native
dependencies before deployment.

API references: https://pak.r-lib.org/reference/lockfile_create.html,
https://pak.r-lib.org/reference/lockfile_install.html,
https://pak.r-lib.org/reference/pak_package_sources.html.
