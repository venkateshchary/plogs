# -*- coding: utf8 -*-

# File: parser.py
# Author: Doug Rudolph
# Created: October 19, 2018

from utils import Table
import pprint


class LogColor:
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    CRITICAL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


class Logger:

    def __init__(self, pretty=True):
        self._pretty = pretty

        self.info = lambda msg: self._log(msg, LogColor.INFO)
        self.success = lambda msg: self._log(msg, LogColor.SUCCESS)
        self.warning = lambda msg: self._log(msg, LogColor.WARNING)
        self.critical = lambda msg: self._log(msg, LogColor.CRITICAL)
        self.status = lambda msg: self._log(msg, LogColor.BOLD)

    def _log(self, msg, log_color):
        log_line = '{}'*3

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
