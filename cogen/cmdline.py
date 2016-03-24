#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author bdepwgjqet[at]gmail.com

import sys
from generator import Generator


def execute(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) == 2:
        engine = Generator(sys.argv[1])
        engine.run()
        print engine.get()
    else:
        print 'Parameter Error'

if __name__ == '__main__':
    execute()
