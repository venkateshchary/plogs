# -*- coding: utf8 -*-

# File: logutils.py
# Author: Doug Rudolph
# Created: October 19, 2018
from enum import Enum

class Levels(Enum):
    INFO = 1
    SUCCESS = 2
    WARNING = 3
    CRITICAL = 4
    STATUS = 5


class Colors:

    _color_map = {
        Levels.INFO: '\033[94m',
        Levels.SUCCESS: '\033[92m',
        Levels.WARNING: '\033[93m',
        Levels.CRITICAL: '\033[91m',
        Levels.STATUS: '\033[1m',
        # Levels.UNDERLINE: '\033[4m',
        'end': '\033[0m',
    }

    @staticmethod
    def color(log_lvl):
        return Colors._color_map[log_lvl]


class LogLevel:

    _level_map = {
        Levels.INFO: '[INFO]: ',
        Levels.SUCCESS: '[SUCCESS]: ',
        Levels.WARNING: '[WARNING]: ',
        Levels.CRITICAL: '[CRITICAL]: ',
        Levels.STATUS: '[STATUS]: ',
    }

    @staticmethod
    def level(log_lvl):
        return LogLevel._level_map[log_lvl]

