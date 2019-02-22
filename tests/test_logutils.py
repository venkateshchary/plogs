# -*- coding: utf8 -*-

# File: plogs/tests/test_logutils.py
# Author: Doug Rudolph
# Created: February 21, 2019

from src import logutils

import unittest


class TestLogger(unittest.TestCase):

    def test_log_levels(self):
        pass

    def test_check_config(self):
        """ Test `check_config` function in `logutils.py` """

        # reference to check_config function
        check_config = logutils.check_config

        # check case where all bool inputs are False
        params = {
            'pretty': False,
            'show_levels': False,
            'show_time': False,
            'to_file': False,
            'file_location': None,
            'filename': None,
        }
        results = check_config(**params)
        compare = zip(params.values(), results)
        for couple in compare:
            self.assertEquals(couple[0], couple[1])
