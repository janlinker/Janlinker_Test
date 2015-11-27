#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
__author__ = 'liaoben'

import pytest

def f():
    raise SystemExit(1)

def test_a():
    print '1'


def test_b():
    print 2