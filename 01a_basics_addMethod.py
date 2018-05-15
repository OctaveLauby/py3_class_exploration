class StupidNumber(object):
    def __init__(self, n):
        self.__n = n

    def __radd__(self, other):
        return self + other

    def __add__(self, other):
        return self.__n + other + 1


sn = StupidNumber(1)
assert 1+sn == 3
assert sn+1 == 3
assert sn._StupidNumber__n == 1
