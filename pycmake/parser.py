# !/bin/env python
# -*- coding: utf-8 -*_
"""

    @FileName: parser.py
    @Author: zlion(zengzs1995@gmail.com)
    @CreatTime: 2018-05-03 16:22:48
    @LastModif: 2018-05-03 16:22:59
    @Note: CMake command parser for cmake project.
"""
import re
import logging


def enumerate_cmake_commands(s, filename):
    off = 0
    lineno = 0

    present_str = s
    if len(present_str) == 0:
        return
    comment_regex = re.compile(r"\s*#(.*?)\n(.*)", flags=re.DOTALL)
    command_regex = re.compile(r"\s*([a-zA-Z_][a-zA-Z0-9_\-]*)\s*\(\s*(.*?)\s*\)(.*)", flags=re.DOTALL)
    # include_regex = re.compile(r"\s*include\s*\(\s*(.*?)\s*\)(.*)", flags=re.DOTALL)
    present_str = present_str.lstrip(" \t\n")

    while len(present_str) != 0:
        comment_match = comment_regex.match(present_str)
        command_match = command_regex.match(present_str)
        # include_match = include_regex.match(present_str)
        if comment_match:
            # Skip the comment line
            comment_line = comment_match.group(1)
            present_str = comment_match.group(2)
        elif command_match:
            command_name = command_match.group(1)
            match_args_line = command_match.group(2)
            present_str = command_match.group(3)
            pass
        else:
            logging.warning("Command_analysis error happen in line: '%s'" % present_str.split("\n")[0])
            i = present_str.find("\n")
            present_str = present_str[i:]


# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
