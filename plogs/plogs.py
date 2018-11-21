# -*- coding: utf8 -*-

# File: plogs.py
# Author: Doug Rudolph
# Created: October 19, 2018

from logutils import LogLevel, Color, Level
from enum import enum
import pprint


class Logger:

    def __init__(self, pretty=True, show_level=False):
        self._pretty = pretty
        self._show_level = show_level

        self.info = lambda msg: self._log(msg, LogLevel.INFO, )
        self.success = lambda msg: self._log(msg, LogLevel.SUCCESS)
        self.warning = lambda msg: self._log(msg, LogLevel.WARNING)
        self.critical = lambda msg: self._log(msg, LogLevel.CRITICAL)
        self.status = lambda msg: self._log(msg, LogLevel.BOLD)


    def _log(self, msg, log_lvl):

        log_line = '{}'*3

        if self.show_level:
            log_line = L

        if self._pretty:
            print(log_line.format(log_color, msg, LogColor.ENDC))
        else:
            print(msg)

    def object(self, obj, params=None, *args):
        key_val_msg = '{}{}{}: {}{}{}'

        if args:
            obj_attrs = vars(obj)

            for arg in args:
                if obj_attrs.get(arg, None):
                    key = arg
                    val = obj_attrs[arg]
                    print(key_val_msg.format(OKBLUE, key, ENDC, FAIL, val, ENDC))

        else:
            for key in sorted(attr):
                print(key_val_msg.format(OKBLUE, key, ENDC, FAIL, attr[key], ENDC))

    def dic(self, dic):
        if self.pretty:
            pass
        else:
            pprint.pprint(dic)


    def table(objs):
        pass
        # define padding
        # find size of header & footer
        # print columns

        """
        +----------------------------+
        | thing | test | test | test |
        """
