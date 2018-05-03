# !/bin/env python
# -*- coding: utf-8 -*_
"""

    @FileName: data.py
    @Author: zlion(zengzs1995@gmail.com)
    @CreatTime: 2018-05-03 16:24:05
    @LastModif: 2018-05-03 16:24:05
    @Note:
"""
import os


class Variables(object):
    def __init__(self, parent=None):
        self._map = {}
        self.__parent = parent


class Target(object):
    def __init__(self):
        pass


class SourceTarget(object):
    pass


class CMakeLists(object):
    def __init__(self, workdir=None, env=None, cmake_flags=""):
        if workdir is None:
            workdir = os.getcwd()
        self.workdir = os.path.realpath(workdir)

        if env is None:
            env = os.environ
        self.env = env

        self.variables = Variables()
        self._targets = dict()
        # TODO: CMake will read environment variables by $ENV{...}

        self.includes = list()


# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
