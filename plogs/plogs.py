#!/usr/bin/env python
# -*- coding: utf8 -*-

""" plogs main python module

File: plogs.py
Author: Doug Rudolph
Created: November 19, 2018


Goals:
    Pretty Logs is a python module that is meant to color code program logs and log files. The main goals
    as a package are:

    1.) 6 easy to understand logging level colors that will color code all of the logs.
        - debug:    Color varies, either no color, or colorcoded object
        - status:   Bold Gray
        - info:     White
        - warning:  Orange
        - error:
        - critical: {{Not Sure Yet}}

    2.) Debugging tools that color code built in python objects: Dictionary and List objects.
    3.) A general set of formatting tools that makes coloring logs intuitive and easy to read.

"""

from logutils import LogLevel, Colors, Levels

import pprint
import sys


class Logger:
    """ Logger class description

    Logger is the main object that gets interfaced with by the user. Logger as an object accepts all
    the settings that formats the logs, writes the log text, and colorcodes text,

    Config Settings:
        There are two main ways to use Pretty Logs

        1.) The first option is to send in an already existing logger, and Pretty Logs will map the default
            logging levels to the proper colors.
            - NOTE*: when doing this a lot of the logging customization is lost, but in return, the original
                     logging settings/formatting is kept, and colors are still applied to your logs.

        2.) The other way to config Pretty Logs is to allow Pretty logs to handle all the general logging settings
            as well as log formatting. By doing this, just be aware that soem formating tools will be not be
            accessible.

    TODO:
        * Add tests
        * Add tables
        * Add default logging wrapper
    """

    def __init__(self, pretty=True, show_levels=True, show_time=False, to_file=False, file_location='/var/log/plogs/'):
        """ Initiliation data for a pretty logger

        Used to configure how the logger writes data to the out

        Args:
            to_file (boolean): writes to logfile -- or to std_out
            file_location (str): custom logfile location -- or None
            pretty (boolean): colored -- uncoloreed
            show_levels (boolean): show levels in output
            show_time (boolean): displays timestamoin the beginning of logline
        """

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
s
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
