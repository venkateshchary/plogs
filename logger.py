# -*- coding: utf8 -*-

# File: parser.py
# Author: Doug Rudolph
# Created: October 19, 2018

from collections import OrderedDict
from utils import Table
import pprint



# HEADER: '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

log_format = '{}'*3

class Logger:

    def __init__(self, pretty=True):
        self.pretty = pretty;

    def success(self, msg):
        print(log_format.format(OKGREEN, msg, ENDC))

    def info(self, msg):
        print(log_format.format(OKBLUE, msg, ENDC))

    def warning(self, msg):
        print(log_format.format(WARNING, msg, ENDC))

    def critical(self, msg):
        print(log_format.format(FAIL, msg, ENDC))

    def underline(self, msg):
        print(log_format.format(UNDERLINE, msg, ENDC))

    def bold(self, msg):
        print(log_format.format(BOLD, msg, ENDC))

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
            attrs = OrderedDict(vars(obj))
            for k, v in attrs.items():
               print(key_val_msg.format(OKBLUE, k, ENDC, FAIL, v, ENDC))

    def dic(self, dic):
        if self.pretty:
            pass
        else:
            pprint.pprint(dic)


    def table(objs):
        # define padding
        # find size of header & footer
        # print columns




       """
       +----------------------------+
       | thing | test | test | test |
       """
