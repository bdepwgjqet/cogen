#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Block(object):

    def __init__(self, lang):
        self.lang = lang
        self.code = []

    def get(self):
        return "".join(self.code)
