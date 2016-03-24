#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path


class Settings(object):
    """
    Store cogen settings
    """

    def __init__(self, fname):
        self.root_file = path.abspath(fname)
        self.project_path = path.dirname(self.root_file)
        self.project_setting = self.project_path + "/settings.py"
