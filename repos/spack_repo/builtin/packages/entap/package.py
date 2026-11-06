# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import gzip
import os
import shutil
import tarfile

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Entap(CMakePackage):
    """Eukaryotic Non-Model Transcriptome Annotation Pipeline.

    Database variants independently install the three components in the EnTAP
    configuration guide. Each downloads fresh data into this spec's prefix;
    previous installations are never searched. Downloads are opt-in because
    EggNOG needs substantial disk space and network access during installation.
    Upstream database endpoints are mutable and have no published checksums;
    these data installations are not reproducible snapshots.

    Copy the installed entap_run.params into a writable working directory and
    pass it with --run-ini. Pass the installed entap_config.ini with --entap-ini,
    or copy and edit it to configure databases omitted during installation.
    RSEM and DIAMOND are separate dependencies (and may be Spack externals).
    TransDecoder 5.7.1 and EggNOG-mapper 2.1.12 use the bundled release archives.
    """

    homepage = "https://entap.readthedocs.io/"
    url = "https://gitlab.com/PlantGenomicsLab/EnTAP/-/archive/v2.3.0/EnTAP-v2.3.0.tar.gz"

    license("GPL-3.0-or-later")
    lmod_template = "entap.lua"
    version("2.3.0", sha256="f040bacafff8945239ce0f398a7440c25f2ae44ecc788b0d8c642502a1229108")

    variant("entap_db", default=False, description="Download the EnTAP binary database")
    variant("eggnog_diamond", default=False, description="Download the EggNOG DIAMOND reference")
    variant("eggnog_sql", default=False, description="Download EggNOG SQL and taxonomy data")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@:3", type="build")
    depends_on("rsem@1.3.3:", type="run")
    depends_on("diamond@2.1.8:", type="run")
    for _database in ("entap_db", "eggnog_diamond", "eggnog_sql"):
        depends_on("curl", when="+" + _database, type="build")

    def cmake_args(self):
        return [
            self.define("ENABLE_TESTING", False),
            self.define("BUILD_STATIC", False),
            self.define("JSON_Install", False),
            self.define("PYTHON_EXECUTABLE", self.spec["python"].command.path),
            self.define("PERL_EXECUTABLE", self.spec["perl"].command.path),
        ]

    @run_after("install")
    def install_support_files(self):
        source = self.stage.source_path
        libexec = self.prefix.libexec.entap
        mkdirp(libexec)
        archives = (
            ("TransDecoder-v5.7.1.tar.gz", "TransDecoder-TransDecoder-v5.7.1", "transdecoder"),
            ("eggnog-mapper-2.1.12.tar.gz", "eggnog-mapper-2.1.12", "eggnog-mapper"),
        )
        for archive, directory, destination in archives:
            with working_dir(self.stage.path):
                which("tar", required=True)("-xf", join_path(source, "libs", archive))
                install_tree(directory, join_path(libexec, destination))

        graph = join_path(self.prefix.bin, "entap_graphing.py")
        install(join_path(source, "src", "entap_graphing.py"), graph)
        # Preserve relative PerlLib/util and eggnogmapper imports.
        for root, _, files in os.walk(libexec):
            for filename in files:
                if filename.endswith((".py", ".pl")) or filename.startswith("TransDecoder."):
                    interpreter = "python" if filename.endswith(".py") else "perl"
                    filter_file(
                        r"^#!.*(?:python\S*|perl)\s*$",
                        "#!" + self.spec[interpreter].command.path,
                        join_path(root, filename),
                    )
        filter_file(r"^#!.*", "#!" + self.spec["python"].command.path, graph)
        filter_file(
            "DIAMOND = find_executable('diamond') or LOCAL_DIAMOND",
            "DIAMOND = " + repr(str(self.spec["diamond"].prefix.bin.diamond)),
            join_path(libexec, "eggnog-mapper", "eggnogmapper", "common.py"),
            string=True,
        )
        mkdirp(self.prefix.db.bin, self.prefix.db.databases)
        config = join_path(self.prefix, "entap_config.ini")
        install(join_path(source, "entap_config.ini"), config)
        install(join_path(source, "entap_run.params"), self.prefix)
        install_tree(
            join_path(source, "test_data"),
            join_path(self.prefix, "build", "entap-" + str(self.version), "test_data"),
        )
        settings = {
            "entap-db-bin": join_path(self.prefix.db.bin, "entap_database.bin"),
            "entap-db-sql": "",
            "entap-graph": graph,
            "diamond-exe": self.spec["diamond"].prefix.bin.diamond,
            "transdecoder-long-exe": join_path(libexec, "transdecoder", "TransDecoder.LongOrfs"),
            "transdecoder-predict-exe": join_path(libexec, "transdecoder", "TransDecoder.Predict"),
            "eggnog-map-exe": join_path(libexec, "eggnog-mapper", "emapper.py"),
            "eggnog-map-data": self.prefix.db.databases,
            "eggnog-map-dmnd": join_path(self.prefix.db.bin, "eggnog_proteins.dmnd"),
        }
        for executable in (
            "rsem-calculate-expression",
            "rsem-sam-validator",
            "rsem-prepare-reference",
            "convert-sam-for-rsem",
        ):
            settings[executable] = join_path(self.spec["rsem"].prefix.bin, executable)
        for key, value in settings.items():
            filter_file("^" + key + "=.*$", key + "=" + str(value), config)

    @run_after("install")
    def install_databases(self):
        """Install only selected components, without invoking the coupled --config."""
        eggnog = "https://eggnog6.embl.de/download/emapperdb-5.0.2/"
        downloads = []
        if "+entap_db" in self.spec:
            downloads.append(
                (
                    "https://treegenesdb.org/FTP/EnTAP/latest/databases/entap_database.bin.gz",
                    join_path(self.prefix.db.bin, "entap_database.bin"),
                )
            )
        if "+eggnog_diamond" in self.spec:
            downloads.append(
                (
                    eggnog + "eggnog_proteins.dmnd.gz",
                    join_path(self.prefix.db.bin, "eggnog_proteins.dmnd"),
                )
            )
        if "+eggnog_sql" in self.spec:
            downloads.append(
                (eggnog + "eggnog.db.gz", join_path(self.prefix.db.databases, "eggnog.db"))
            )
            # EggNOG-mapper also requires its taxonomy database.
            downloads.append((eggnog + "eggnog.taxa.tar.gz", None))
        if not downloads:
            return
        mkdirp(self.prefix.db.bin, self.prefix.db.databases)
        curl = Executable(self.spec["curl"].prefix.bin.curl)
        for url, destination in downloads:
            archive = join_path(self.stage.path, url.rsplit("/", 1)[1])
            curl("--fail", "--location", "--retry", "3", "--output", archive, url)
            if destination:
                with gzip.open(archive, "rb") as src, open(destination, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                if url.endswith("entap_database.bin.gz"):
                    # Refuse future incompatible data from the mutable latest endpoint.
                    with open(destination, "rb") as database:
                        header = [database.readline().strip() for _ in range(2)]
                    if header != [b"VERSION_MAJOR=3", b"VERSION_MINOR=0"]:
                        raise InstallError("EnTAP 2.3.0 requires binary database format 3.0")
            else:
                with tarfile.open(archive, "r:gz") as data:
                    for member in data.getmembers():
                        if member.isdir():
                            continue
                        name = os.path.normpath(member.name)
                        if not member.isfile() or os.path.basename(name) != name:
                            raise InstallError("Unexpected EggNOG taxonomy archive member")
                        with data.extractfile(member) as src:
                            with open(join_path(self.prefix.db.databases, name), "wb") as dst:
                                shutil.copyfileobj(src, dst)
            os.remove(archive)

    def setup_run_environment(self, env):
        env.set("ENTAP_CONFIG", join_path(self.prefix, "entap_config.ini"))
        env.set("RUN_PARAMS", join_path(self.prefix, "entap_run.params"))
        env.set(
            "ENTAP_TESTDATA",
            join_path(self.prefix, "build", "entap-" + str(self.version), "test_data"),
        )
        env.set("ENTAP_DB", self.prefix.db)
        env.prepend_path("PATH", join_path(self.prefix.libexec.entap, "transdecoder"))
        env.prepend_path("PATH", join_path(self.prefix.libexec.entap, "eggnog-mapper"))
