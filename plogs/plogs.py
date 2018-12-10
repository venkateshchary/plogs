#!/usr/bin/env python
# -*- coding: utf8 -*-

from logutils import LogLevel, Colors, Levels

import pprint
import datetime
import pdb


# global reference to logger (this is because _Logger is a singleton)
_LOGGER_REF = None


def get_logger():
    global _LOGGER_REF

    if _LOGGER_REF is None:
        _LOGGER_REF = _Logger()

    return _LOGGER_REF


class _Logger:

    def __init__(self):
        # Instances of Color and Levels enum
        self._colors = Colors.color
        self._levels = LogLevel.level

        # Name of default log file is plogs_<datetime>
        self._filename = '{}_{}'.format(
            'plogs', str(datetime.datetime.now().date()),
        )

        # These are the default configs
        self._show_levels = False
        self._show_time = False
        self._pretty = True

        self._to_file = False
        self._file_location = '/var/log/plogs/'
        self._fstr = None
        self._default_logger = None

        # define log function for each log level
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
        self._fstr = fstr

    def bind(self, logger):
        # self.logger = logger
        pass

    def _format(self, msg, log_lvl):
        log = msg

        # {{NOTE: any log variables that are added must be get appended in here}}
        if self._fstr:
            log = self._fstr
            if self._show_levels: log = log.replace('{level}', self._levels(log_lvl))
            if self._show_time: log = log.replace('{time}', str(datetime.datetime.now()))
            if self._file_location: log = log.replace('{filename}', self._file_location)

            # always need to replace msg
            log = log.replace('{msg}', msg)

        # colors the logs if self_.pretty == True
        if self._pretty:
            log = self._colors(log_lvl) + log + self._colors('end')

        return log

    def _log(self, msg, log_lvl):
        log = self._format(msg, log_lvl)

        # open and write to file if set to
        if self._to_file:
            file_dest = f'{self._filename}{self.file_location}'
            with open(file_dest, 'w+') as fd:
                fd.write(log + '\n')
        else:
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
        if self._pretty:
            pass
        else:
            pprint.pprint(dic)


    def table(objs):
        pass
        # define padding
        # find size of header & footer
        # print columns
