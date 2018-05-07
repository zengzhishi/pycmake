# !/bin/env python
# -*- coding: utf-8 -*_
"""

    @FileName: util.py
    @Author: zlion(zengzs1995@gmail.com)
    @CreatTime: 2018-05-03 16:24:50
    @LastModif: 2018-05-03 16:24:50
    @Note:
"""

import os
import re


def unbalanced_quotes(s):
    single = 0
    double = 0
    excute = 0
    for c in s:
        if c == "'":
            single += 1
        elif c == '"':
            double += 1
        elif c == "`":
            excute += 1

    move_double = s.count('\\"')
    move_single = s.count("\\'")
    single -= move_single
    double -= move_double

    is_half_quote = single % 2 == 1 or double % 2 == 1 or excute % 2 == 1
    return is_half_quote


def split_line(line):
    # Pass 1: split line using whitespace
    words = line.strip().split()
    # Pass 2: merge words so that the no. of quotes is balanced
    res = []
    for w in words:
        if len(res) > 0 and unbalanced_quotes(res[-1]):
            res[-1] += " " + w
        else:
            res.append(w)
    return res


def strip_quotes(s):
    if s[0] == "'" and s[-1] == "'":
        return s[1:-1]
    elif s[0] == '"' and s[-1] == '"':
        return s[1:-1]
    else:
        return s

# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
