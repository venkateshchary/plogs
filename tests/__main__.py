import sys
sys.path.append('../src/')

from . import test_logutils, test_tableutils


def main():
    # reference `run_tests` function in each test file
    tests = [
        test_logutils.run_tests,
        test_tableutils.run_tests,
    ]

    # run each test
    for test in tests:
        test()

if __name__ == '__main__':
    main()
