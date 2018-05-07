# !/bin/env python
# -*- coding: utf-8 -*_
"""

    @FileName: commands.py
    @Author: zlion(zengzs1995@gmail.com)
    @CreatTime: 2018-05-03 17:19:41
    @LastModif: 2018-05-03 17:19:41
    @Note:
"""
import pycmake.util as util


class Command(object):
    def __init__(self, name, args_line):
        self.command_name = name
        self.fields = util.split_line(args_line)


# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
