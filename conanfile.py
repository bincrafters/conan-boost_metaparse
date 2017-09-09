from conans import ConanFile, tools, os

class BoostMetaparseConan(ConanFile):
    name = "Boost.Metaparse"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-metaparse"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["metaparse"]
    requires =  "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Test/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing"

                      #config0 mpl5 predef0 preprocessor0 static_assert1 type_traits3

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()