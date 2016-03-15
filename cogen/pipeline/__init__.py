#!/usr/bin/env python
# -*- coding: utf-8 -*-


class pipeline(object):

    def __init__(self, blocks):
        self.queue = blocks

    def run(self):
        lines = []
        while self.queue:
