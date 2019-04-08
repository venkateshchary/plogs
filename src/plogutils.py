# -*- coding: utf8 -*-

# File: plogutils.py
# Author: Doug Rudolph
# Created: November 19, 2018


from .logutils import Levels, Colors, check_config
from .tableutils import construct_table

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

    def info(self, msg):
        self._log(msg, Levels.INFO)

    def success(self, msg):
        self._log(msg, Levels.SUCCESS)

    def warning(self, msg):
        self._log(msg, Levels.WARNING)

    def critical(self, msg):
        self._log(msg, Levels.CRITICAL)

    def error(self, msg):
        self._log(msg, Levels.ERROR)

    def status(self, msg):
        self._log(msg, Levels.STATUS)

    def table(self, objects):
        table_str = construct_table(objects)
        self._log(table_str, Levels.STATUS)

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
        """ Binds already existing logger to plogs logger """
        self.logger = logger

        self.info = self.logger.info
        self.status = self.logger.status
        self.succeses = self.logger.success
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.critical = self.logger.critical

    def _format(self, msg, log_lvl):
        log_msg = str(msg)

        # NOTE: any `log_msg` variables that are added to `__init__`
        # must also have an if statement and or included in the
        # _fstr.format function call
        if self._fstr:
            log_msg = self._fstr.format(
                level=self._levels(log_lvl),
                time=str(datetime.datetime.now()),
                filename=self._filename,
                msg=msg
            )

        # colors the `log_msg` if self._pretty == True
        if self._pretty:
            end_color = str(Colors.END)
            log_msg = self._colors(log_lvl) + log_msg + end_color

        return log_msg

    def _log(self, msg, log_lvl):
        # - Attempt to format the log
        #   nothing will happen if no format vars have been set
        # - Also ensure that the entire log is of type strings
        log = self._format(msg, log_lvl)
        log = str(log)

        # open and write to file if set to
        if self._to_file:
            file_dest = '{}{}'.format(self._file_location, self._filename)
            with open(file_dest, 'a+') as fd:
                fd.write(log + '\n')
        else:
            print(log)
