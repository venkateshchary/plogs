# -*- coding: utf8 -*-

# File: error.py
# Author: Doug Rudolph
# Created: March 31, 2019

def trace(func):
    """ Format error message of a function """
    try:
        func()
    except Exception as err:
        traceback = err.__traceback__

        # iterate over traceback until there are no more errors in list
        while traceback:
            dir(traceback)
            # filename = traceback.tb_frame.f_code.co_filename
            # line_num = traceback.tb_lineno

            # err_msg = f'\nFile "{filename}", line {line_num}, {function}\n'
            # print(err_msg)

            traceback = traceback.tb_next

