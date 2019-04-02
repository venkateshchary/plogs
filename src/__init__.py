# -*- coding: utf8 -*-

# File: plogutils.py
# Author: Doug Rudolph
# Created: November 19, 2018

name = 'plogs'
__all__ = ['plogutils.py', 'logutils.py', 'tableutils.py', 'errorutils.py']


from .plogutils import _get_logger
from .errorutils import _functrace


def trace(func):

    def wrapper(*args, **kwargs):
        return _functrace(func)

    return wrapper


def get_logger():
    return _get_logger()
