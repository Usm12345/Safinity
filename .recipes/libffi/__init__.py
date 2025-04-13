from pythonforandroid.recipe import CythonRecipe


class LibffiRecipe(CythonRecipe):
    version = "3.4.4"
    url = "https://github.com/libffi/libffi/releases/download/v{version}/libffi-{version}.tar.gz"
    depends = []
    patches = []

    def build_arch(self, arch):
        # Skip autogen and use provided configure
        super().build_arch(arch)


recipe = LibffiRecipe()
