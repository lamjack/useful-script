#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, commands

work_path = os.path.abspath(os.getcwd())
cmd = "find %s -name \".DS_Store\" -depth -exec rm {} \;" % work_path
commands.getoutput(cmd)
print cmd