#!/usr/bin/env python
# -*- coding: utf-8 -*-

from settings import Settings
import imp
import reader
import config
import sys
import StringIO
import contextlib


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


class Generator(object):

    def __init__(self, fname):
        self.settings = Settings(fname)
        self.code = []

    def load_project_settings(self):
        imp.load_source('prosettings', self.settings.project_setting)

    def run_once(self, root):
        blocks = reader.read_blocks(root)
        code = []
        for block in blocks:
            if block.lang == "python":
                with stdoutIO() as s:
                    import prosettings
                    exec block.get()
                code.append(s.getvalue())
                code.append(config.cobody)
                code.append(config.cobody)
            elif block.lang == "file":
                engine = Generator(block.get().rstrip())
                engine.run()
                code.append(engine.get())
            else:
                code.append(block.get().rstrip())
        return code

    def run(self):
        self.load_project_settings()
        self.code.append(config.cohead)
        self.code.append(config.cobody)
        self.code += self.run_once(self.settings.root_file)

    def get(self):
        return "\n".join(self.code)
