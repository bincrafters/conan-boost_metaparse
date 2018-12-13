#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostMetaparseConan(base.BoostBaseConan):
    name = "boost_metaparse"
    url = "https://github.com/bincrafters/conan-boost_metaparse"
    lib_short_names = ["metaparse"]
    header_only_libs = ["metaparse"]
    b2_requires = [
        "boost_config",
        "boost_mpl",
        "boost_predef",
        "boost_preprocessor",
        "boost_static_assert",
        "boost_type_traits"
    ]
