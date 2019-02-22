# -*- coding: utf8 -*-

# File: plogs/tests/__main__.py
# Author: Doug Rudolph
# Created: February 21, 2019

import sys
sys.path.append('../src/')

from unittest import TextTestRunner, TestSuite, TestLoader

from .test_logutils import TestLogger
from .test_tableutils import TestTable


def create_test_suite():
    """ Creates test suite and adds test cases"""

    test_cases = (TestLogger, TestTable)
    test_suite = TestSuite()
    test_loader = TestLoader()

    for test_case in test_cases:
        tests = test_loader.loadTestsFromTestCase(test_case)
        test_suite.addTest(tests)

    return test_suite

def run_tests():
    """ Get plogs test suite and run all tests """

    # create test suite
    test_suite = create_test_suite()

    # run test suite
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

if __name__ == '__main__':
    run_tests()
