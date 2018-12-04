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
        - error:    {{Not Sure Yet}}
        - critical: Red

    2.) Debugging tools that color code built in python objects: Dictionary and List objects.
    3.) A general set of formatting tools that makes coloring logs intuitive and easy to read.

"""

from logutils import LogLevel, Colors, Levels

import pprint
import sys


_LOGGER_REF = None


def get_logger():
    global _LOGGER_REF

    if _LOGGER_REF is None:
        _LOGGER_REF = _Logger()

    return _LOGGER_REF


class _Logger:
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

    def __init__(self):
        # instances of Color and levels enum
        self._colors = Colors.color
        self._levels = LogLevel.level

        # These are the default configs
        self._pretty = True
        self._show_levels = False
        self._show_time = False
        self._to_file = False
        self._file_location = '/var/log/plogs/'
        self._fstr = None
        self._default_logger = None

        # define log functino for each log level
        self.info = lambda msg: self._log(msg, Levels.INFO)
        self.status = lambda msg: self._log(msg, Levels.STATUS)
        self.success = lambda msg: self._log(msg, Levels.SUCCESS)
        self.warning = lambda msg: self._log(msg, Levels.WARNING)
        self.error = lambda msg: self._log(msg, Levels.ERROR)
        self.critical = lambda msg: self._log(msg, Levels.CRITICAL)

    def config(self, pretty=True, show_levels=False, show_time=False, to_file=False, file_location='/var/log/plogs/'):
        self._pretty = pretty
        self._show_levels = show_levels
        self._show_time = show_time
        self._to_file = to_file
        self._file_location = file_location

    def format(self, fstr):
        """ Customizes the output of the log string """
        self.fstr = fstr

    def bind(self, logger):
        """ The purpose of this binding function is to be able to use
        the default logger that's built into python, along side Pretty
        Logs

        Args:
            logger (logging): Instance of built in python logger
        """
        # self.logger = logger
        pass

    def _log(self, msg, log_lvl):
        formatted_log = '{}'*3
        log = msg

        if self._pretty:
            log_color = self._colors(log_lvl)
            end_color = self._colors('end')
            log = formatted_log .format(log_color, msg, end_color)

        print(log)


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
