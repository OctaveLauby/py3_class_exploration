from time import time


class A(object):
    def __init__(self):
        self.time = 1


class B(object):
    @property
    def time(self):
        return time()


a = A()
b = B()

print(a.time, b.time)
