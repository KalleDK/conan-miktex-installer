from conans import ConanFile, tools
import os


class MiktexinstallerConan(ConanFile):
    name = "miktex_installer"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/KalleDK/conan-miktex-installer"
    settings = {"os": ["Windows"]}
    build_policy = "missing"
    
    def configure(self):
        self.requires.add("7z_installer/0.1@lasote/testing", private=True)

    def build(self):
        url = "http://mirror.physik-pool.tu-berlin.de/tex-archive/systems/win32/miktex/setup/miktex-portable-2.9.6326.exe"
        tools.download(url, "file.exe")
        self.run("7z x file.exe")
        

    def package(self):
        self.copy("*", dst="", src="texmfs")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "install", "miktex", "bin"))
