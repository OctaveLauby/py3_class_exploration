class A():
    a = 0


class B(A):
    pass


class C(B):
    pass


class D(A):
    a = 0
    pass


A.a += 1
B.a += 2
D.a += 2
C.a += 4

assert A.a == 1  # Is not influenced by subclasses updates
assert B.a == 3  # Was influenced by A update
assert C.a == 7  # Was influence by A-B updates
assert D.a == 2  # Was NOT influenced by A

print(A.__subclasses__())
