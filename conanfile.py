import os
from conans import ConanFile, tools


class GliConan(ConanFile):
    name = "gli"
    version = "0.8.2.0"
    url = "https://github.com/g-truc/gli"
    description = "OpenGL Image (GLI) http://gli.g-truc.net"
    requires = "glm/0.9.9.8"
    no_copy_source = True

    def source(self):
        tools.get(f'{self.url}/archive/{self.version}.zip')

    def package(self):
        include_folder = os.path.join(
            self.source_folder, f'{self.name}-{self.version}', 'gli')
        self.copy(pattern='*.h', dst='include/gli', src=include_folder)
        self.copy(pattern='*.hpp', dst='include/gli', src=include_folder)
        self.copy(pattern='*.inl', dst='include/gli', src=include_folder)

    def package_id(self):
        self.info.header_only()

