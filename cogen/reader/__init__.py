#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import config
from blocker import Block
from config import lamark
from config import laend


def read_blocks(fpath):

    with open(fpath) as f:
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
            block = Block(config.laraw)
            block.code.append(line)
            blocks.append(block)

    return blocks
