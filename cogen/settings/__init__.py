#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path


class Settings(object):
    """
    Store cogen settings
    """

    def __init__(self, fname):

        # project_path - the absolute path where you exec cogen
        self.project_path = path.abspath('.')

        # project_setting - setting .py file under project_path
        self.project_setting = self.project_path + "/settings.py"

        # current template path
        self.root_file = path.abspath(fname)
