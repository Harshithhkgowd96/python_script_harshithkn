class TestingExamples:
    def _init_(self, pkg_name, version):
        self.name = pkg_name
        self.version = version

    def check_artifact(self):
        print(f"The package name is {self.name}")
        print(f"THE version is {self.version}")

    def print_combine(self):
        print(f"The package name with version {self.name}:{self.version}")

if _name_ == "_main_":

    package = input("Enter the package Name\n")
    version = input("ENter the version\n")
    check = TestingExamples(package, version)

    check.check_artifact()
    check.print_combine()
