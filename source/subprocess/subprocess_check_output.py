#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""
Capture the output of a command and test its
exit code at the same time.
"""
#end_pymotw_header

import subprocess

output = subprocess.check_output(['ls', '-1'])
print('Have {} bytes in output'.format(len(output)))
print(output.decode('utf-8'))
