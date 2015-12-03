#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
__author__ = 'liaoben'

import subprocess
import os
# print ’popen3:’
def external_cmd(cmd, msg_in=''):
    try:
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
        stdout_value, stderr_value = proc.communicate(msg_in)
        return stdout_value, stderr_value
    except ValueError, err:
        # log("IOError: %s" % err)
        return None, None

if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))+'\\Scripts\\BasicFunctionTest'
    print path
    cmd = 'nosetests -s -w '+path
    stdout_val, stderr_val = external_cmd(cmd)
    print 'Standard Output: %s' % stdout_val
    print 'Standard Error: %s' % stderr_val
