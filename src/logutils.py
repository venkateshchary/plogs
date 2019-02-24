# -*- coding: utf8 -*-

# File: logutils.py
# Author: Doug Rudolph
# Created: November 19, 2018


from enum import Enum

import os


class Levels(Enum):
    INFO = 1
    SUCCESS = 2
    WARNING = 3
    CRITICAL = 4
    ERROR = 5
    STATUS = 6

    def level(self):
        return self.name

    def color(self):
        # TODO: fix the fact that passing in 'end' is necessary and "proper use."
        _color_map = {
            Levels.INFO: '\033[94m',
            Levels.STATUS: '\033[1m',
            Levels.SUCCESS: '\033[92m',
            Levels.WARNING: '\033[93m',
            Levels.ERROR: '\033[91m',
            Levels.CRITICAL: '\u001b[41;1m',
        }
        return _color_map[self]


def check_config(pretty=True, show_levels=False, show_time=False, to_file=False, file_location=None, filename=None):

    # if trying to write to file, the following cases must hold true
    if to_file:

       # file_location and filename must be strings
        if not isinstance(file_location, str) or not isinstance(filename, str):
            raise TypeError('`filename` or `file_location` must be a non-empty string')
        elif len(file_location) == 0 or len(filename) == 0:
            raise ValueError('`filename` or `file_location` must be a non-empty string')

        # file_location must exist
        if not os.path.exists(file_location):
            # assumes that the error will just raise
            os.mkdir(file_location)

    # config variables must be type `bool`
    if not isinstance(pretty, bool) or not isinstance(show_levels, bool)\
            or not isinstance(show_time, bool) or not isinstance(to_file, bool):
        raise TypeError(
            'One of the following config variables is not of type `bool`:\n ' +\
            'pretty: ' + pretty + '\n' +\
            'show_levels: ' + show_levels + '\n' +\
            'show_time: ' + show_time + '\n' +\
            'to_file: ' + to_file
        )

    # return updated vars
    return pretty, show_levels, show_time, to_file, file_location, filename
