import sys
sys.path.append('../src/')

from . import test_logutils
from . import test_tableutils


def main():
    tests = [
        test_logutils.run_tests,
        test_tableutisl.run_tests,
    ]

    for test in tests:
        test()

if __name__ == '__main__':
    main()
