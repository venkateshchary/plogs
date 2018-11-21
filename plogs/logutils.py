# -*- coding: utf8 -*-

# File: logutils.py
# Author: Doug Rudolph
# Created: October 19, 2018

class LogLevel(Enum):
    INFO = 1
    SUCCESS = 2
    WARNING = 3
    CRITICAL = 4
    STATUS = 5


class Color:

    def __init__(self):
        self.color_map = {
            LogLevel.INFO = '\033[94m'
            LogLevel.SUCCESS = '\033[92m'
            LogLevel.WARNING = '\033[93m'
            LogLevel.CRITICAL = '\033[91m'
            LogLevel.BOLD = '\033[1m'
            LogLevel.UNDERLINE = '\033[4m'
            LogLevel.ENDC = '\033[0m'
        }

    def color(self, log_lvl):
        return self.color_map[log_lvl]


class Level:

    def __init__(self):
        self.level_map = {
            LogLevel.INFO: '[INFO]: ',
            LogLevel.SUCCESS: '[SUCCESS]: ',
            LogLevel.WARNING: '[WARNING]: ',
            LogLevel.CRITICAL: '[CRITICAL]: ',
            LogLevel.STATUS: '[STATUS]: ',
        }

    def level(self, log_lvl):
        return self.level_map[log_lvl]

