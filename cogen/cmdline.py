#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author bdepwgjqet[at]gmail.com

import sys
import reader


def execute(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) == 2:
        blocks = reader.read_blocks(argv[1])
        for block in blocks:
            print block.lang
            for line in block.code:
                print line
            print "====="
    else:
        print 'Parameter Error'

if __name__ == '__main__':
    execute()
