#!/usr/bin/env python
# -*- coding: utf8 -*-

from .logutils import Levels, check_config

import pprint
import datetime


# global reference to logger (this is because _Logger is a singleton)
_LOGGER_REF = None


def _get_logger():
    global _LOGGER_REF

    if _LOGGER_REF is None:
        _LOGGER_REF = _Logger()

    return _LOGGER_REF


class _Logger:

    def __init__(self):
        # Instances of Color and Levels enum
        self._colors = Levels.color
        self._levels = Levels.level

        # Formatting variables
        self._show_levels = False
        self._show_time = False
        self._pretty = True

        # Config Varables
        self._to_file = False
        self._file_location = '/var/log/plogs/'
        self._filename = 'plogs_01.log'
        self._fstr = None
        self._logger = None

        # define log function for each log level
        self.info = lambda msg: self._log(msg, Levels.INFO)
        self.status = lambda msg: self._log(msg, Levels.STATUS)
        self.success = lambda msg: self._log(msg, Levels.SUCCESS)
        self.warning = lambda msg: self._log(msg, Levels.WARNING)
        self.error = lambda msg: self._log(msg, Levels.ERROR)
        self.critical = lambda msg: self._log(msg, Levels.CRITICAL)

    def config(self, pretty=True, show_levels=False, show_time=False, to_file=False, file_location='/var/log/plogs/', filename='plogs_01.log'):
        # check all possible issue with config variables

        pretty, show_levels, show_time, to_file, file_location, filename = \
            check_config(pretty, show_levels, show_time, to_file, file_location, filename)

        # store config variables
        self._pretty = pretty
        self._show_levels = show_levels
        self._show_time = show_time
        self._to_file = to_file
        self._file_location = file_location
        self._filename = filename

    def format(self, fstr):
        self._fstr = fstr

    def bind(self, logger):
        self.logger = logger

        self.info = self.logger.info
        self.status = self.logger.status
        self.succeses = self.logger.success
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.critical = self.logger.critical

    def _format(self, msg, log_lvl):
        log = msg

        # {{NOTE: any log variables that are added must be get appended in here}}
        if self._fstr:
            log = self._fstr.format(level=self._levels(log_lvl),
                    time=str(datetime.datetime.now()), filename=self._filename, msg=msg)

        # colors the logs if self_.pretty == True
        if self._pretty:
            log = self._colors(log_lvl) + log + self._colors('end')

        return log

    def _log(self, msg, log_lvl):
        log = self._format(msg, log_lvl)

        # open and write to file if set to
        if self._to_file:
            file_dest = '{}{}'.format(self._file_location, self._filename)
            with open(file_dest, 'a+') as fd:
                fd.write(log + '\n')
        else:
            print(log)
