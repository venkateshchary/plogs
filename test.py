import logger
from pprint import pprint

class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


a = A(1, 2, 3)
# pprint(vars(a))
logger.object(a)
