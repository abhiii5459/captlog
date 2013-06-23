#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of caplog.
#
# caplog - Captain's Log (secret diary and notes application)
#
# Written in 2013 by Ricardo Garcia <public@rg3.name>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with
# this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.

class LogEntry(object):
    def __init__(self, id_le, ctime, mtime, data=None):
        self.id_le = id_le
        self.ctime = ctime
        self.mtime = mtime
        self.data = data

    def __cmp__(self, other):
        return cmp(self.ctime, other.ctime)

class Bookmark(object):
    def __init__(self, id_bm, id_le, text):
        self.id_bm = id_bm
        self.id_le = id_le
        self.text = text

    def __cmp__(self, other):
        return cmp(self.text, other.text)