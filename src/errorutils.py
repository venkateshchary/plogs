# -*- coding: utf8 -*-

# File: error.py
# Author: Doug Rudolph
# Created: March 31, 2019

import linecache

def _functrace(func, *args, **kwargs):
    """ Function decorator that formats the stack trace of a function
    if an exception is thrown.

    Example:
        >>> @plogs.trace
        >>> def cause_error():
        >>>     error = 1/0
        >>>
        >>> # Results in formatted stack trace

    Args:
        func (function): decorated function
        args (*var): arguments that might be in `func`
        kwargs (**var): keyword arguments that might be in `func`

    TODO:
        *print the exception name
        *get the module name in the output
        *actually color code output
    """
    try:
        # try running decorated function and see if an error occurs
        result = func(*args, **kwargs)
        return result

    except Exception as err:
        # get the traceback object from the error
        # and make sure the current function call is not apart of the stack trace
        traceback = err.__traceback__
        traceback = traceback.tb_next

        import pdb
        pdb.set_trace()

        while traceback:
            # get the stack frame, filename, and line number of error
            frame = traceback.tb_frame
            filename = traceback.tb_frame.f_code.co_filename
            lineno = traceback.tb_lineno

            # Step into the line cache to get the source code of the error
            linecache.checkcache(filename)
            src_code = linecache.getline(filename, lineno, frame.f_globals)

            # generate and print error message
            err_msg = f'File "{filename}", line {lineno}, ...\n{src_code}'
            print(err_msg)

            # go to next stack frame
            traceback = traceback.tb_next

        # log final error message
        exception = str(err.__class__.__name__)
        exception_msg = str(err)
        err_msg = f'{exception}: {exception_msg}'
        print(err_msg)
