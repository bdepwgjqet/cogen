#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import settings
from blocker import Block
from settings import lamark
from settings import laend


def read_blocks(fname):
    path = os.path.abspath(fname)

    with open(path) as f:
        lines = f.readlines()

    inblock = False
    blocks = []
    block = None
    for line in lines:
        lkey = line.rstrip()
        if inblock:
            if laend == lkey:
                blocks.append(block)
                inblock = False
            else:
                block.code.append(line)
            continue
        if lamark.has_key(lkey):
            block = Block(lamark.get(lkey))
            inblock = True
        else:
            block = Block(settings.laraw)
            block.code.append(line)
            blocks.append(block)

    return blocks
