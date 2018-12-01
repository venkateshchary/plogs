#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
File: plogs.py
Author: Doug Rudolph
Created: October 19, 2018
"""

import pprint
import sys

from logutils import LogLevel, Colors, Levels




class Logger:
    """
    Config Settings:
        There are two main ways to use Pretty Logs, you can either can send in an already existing logger,
        and Pretty Logs will map the logging levels to the proper colors schemes. When doing this,
        a lot of the logging customization is lost, but in return, the original logging settings/formatting is kept,
        and colors are applied to your logs.

        The other way to config pretty logger is to allow Pretty logs to handle the settings.

    - to_file: stdout or a file
    - pretty: colored or uncolored
    - show_levels: show levels in output
    - __: app
    - show_time
    """

    def __init__(self, pretty=True, show_levels=True, show_time=True, to_file=False, traditional=False):

        self.colors = None if not pretty else Colors.color
        self.levels =  None if not show_levels else LogLevel.level

        self._pretty = pretty
        self._show_levels = show_levels

        self.info = lambda msg: self._log(msg, Levels.INFO)
        self.status = lambda msg: self._log(msg, Levels.STATUS)
        self.success = lambda msg: self._log(msg, Levels.SUCCESS)
        self.warning = lambda msg: self._log(msg, Levels.WARNING)
        self.critical = lambda msg: self._log(msg, Levels.CRITICAL)


    def _log(self, msg, log_lvl):
        log_line = '{}'*3

        if self._show_levels:
            log_line = self.levels(log_lvl) + log_line  # show log level in line

        if self._pretty:
            log_color = self.colors(log_lvl)  # gets color based on log level
            end_color = self.colors('end')  # add to end of line to stop writing in color
            log_msg = log_line.format(log_color, msg, end_color)
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
