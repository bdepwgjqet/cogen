#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author bdepwgjqet[at]gmail.com

import sys
import imp
from os import path
import reader
from settings import cohead
from settings import cobody


def execute(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) == 2:
        templatep = path.abspath(sys.argv[1])
        confp = path.dirname(templatep) + "/settings.py"
        imp.load_source('tsettings', confp)

        import tsettings

        blocks = reader.read_blocks(argv[1])
        print cohead
        print cobody
        for block in blocks:
            if block.lang == "python":
                exec block.get()
                print cobody
                print cobody
            else:
                print block.get().rstrip()
    else:
        print 'Parameter Error'

if __name__ == '__main__':
    execute()
