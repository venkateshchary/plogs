# -*- coding: utf8 -*-

# File: plogs/tests/test_logutils.py
# Author: Doug Rudolph
# Created: February 21, 2019

from src import logutils

import unittest
import os


class TestLogger(unittest.TestCase):

    def test_file_writing(self):
        """ Tests `check_config` recognizes a file does and doesn't exist """
        # reference to check_config function
        check_config = logutils.check_config

        # check case where all bool inputs are False
        file_location = './'
        filename = 'i_dont_exist.txt'

        params = {
            'pretty': False,
            'show_levels': False,
            'show_time': False,
            'to_file': True,
            'file_location': file_location,
            'filename': filename,
        }
        check_config(**params)
        self.assertFalse(os.path.exists(file_location+filename))

    def test_file_writing_errors(self):
        """ Tests `check_config` file writing cases that return errors """

        # reference to check_config function
        check_config = logutils.check_config

        # check case where all bool inputs are False
        params = {
            'pretty': False,
            'show_levels': False,
            'show_time': False,
            'to_file': True,
            'file_location': '',
            'filename': '',
        }
        with self.assertRaises(ValueError):
            check_config(**params)

        # check case where all bool inputs are False
        params = {
            'pretty': False,
            'show_levels': False,
            'show_time': False,
            'to_file': True,
            'file_location': dict,
            'filename': dict,
        }
        with self.assertRaises(TypeError):
            check_config(**params)

    def test_formatting(self):
        """ Test formatting vars in `check_config` """

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
        results = dict(zip(params.keys(), check_config(**params)))
        self.assertFalse(results['pretty'])
        self.assertFalse(results['show_levels'])
        self.assertFalse(results['show_time'])
        self.assertFalse(results['to_file'])
        self.assertIsNone(results['file_location'])
        self.assertIsNone(results['filename'])

        # check case where inputs are True inputs are False
        params = {
            'pretty': True,
            'show_levels': True,
            'show_time': True,
            'to_file': False,
            'file_location': None,
            'filename': None,
        }
        results = dict(zip(params.keys(), check_config(**params)))
        self.assertTrue(results['pretty'])
        self.assertTrue(results['show_levels'])
        self.assertTrue(results['show_time'])
        self.assertFalse(results['to_file'])
        self.assertIsNone(results['file_location'])
        self.assertIsNone(results['filename'])
