# -*- coding: utf8 -*-

# File: test_logutils.py
# Author: Doug Rudolph
# Created: February 21, 2019

import unittest

from src import logutils


class TestLogger(unittest.TestCase):

    def test_log_levels(self):
        pass

    def test_log_config(self):
        """ Test `check_config` functio in `logutils.py` """

        # reference to check_config function
        check_config = logutils.check_config

        # check when all bool vals are False
        params = {
            'pretty': False,
            'show_levels': False,
            'show_time': False,
            'to_file': False,
            'file_location': None,
            'file_name': None,
        }
        results = check_config(**params)
        compare_seq = zip(params.values(), results)
        map(compare_seq, lambda x: self.assertEquals(x[0], x[1]))


def run_tests():
    unittest.main()
