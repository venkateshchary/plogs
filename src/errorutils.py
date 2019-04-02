# -*- coding: utf8 -*-

# File: error.py
# Author: Doug Rudolph
# Created: March 31, 2019

import linecache

def functrace(func):
    """ Function decorator that formats the stack trace of a function
    if an exception is thrown.

    Example:
        >>> @plogs.trace
        >>> def cause_error():
        >>>     error = 1/0
        >>>
        >>> # Restults in formatted stacktrace

    Args:
        func (function): decorated function

    Returns:
        void: if no error is thrown, or halts program if error is thrown
    """

    try:
        func()
    except Exception as err:

        traceback = err.__traceback__
        while traceback:
            frame = traceback.tb_frame
            filename = traceback.tb_frame.f_code.co_filename
            lineno = traceback.tb_lineno

            linecache.checkcache(filename)
            line_src = linecache.getline(filename, lineno, frame.f_globals)

            err_msg = f'File "{filename}", line {lineno}, ...\n{line_src}\n'
            print(err_msg)

            traceback = traceback.tb_next
