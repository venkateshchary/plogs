# -*- coding: utf8 -*-

# File: parser.py
# Author: Doug Rudolph
# Created: October 19, 2018


# HEADER: '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

log_format = '{}'*3

def success(msg):
    print(log_format.format(OKGREEN, msg, ENDC))


def info(msg):
    print(log_format.format(OKBLUE, msg, ENDC))


def warning(msg):
    print(log_format.format(WARNING, msg, ENDC))


def warning(msg):
    print(log_format.format(FAIL, msg, ENDC))


def underline(msg):
    print(log_format.format(UNDERLINE, msg, ENDC))


def bold(msg):
    print(log_format.format(BOLD, msg, ENDC))


# TODO: log an objects values in a table view
