"""
Parent1 \
           Child
Parent2 /
"""


# ---- Simple case
# Parent1 \
#            Child
# Parent2 /

class Parent1(object):
    pass


class Parent2(object):
    pass


class Child(Parent1, Parent2):
    pass


if __name__ == '__main__':
    assert Child.mro() == [Child, Parent1, Parent2, object]


# ---- Deep case
# Parent1 > Child1 \
#                     GrandChild
# Parent2 > Child2 /
class Parent1(object):
    pass


class Child1(Parent1):
    pass


class Parent2(object):
    pass


class Child2(Parent2):
    pass


class GrandChild(Child1, Child2):
    pass


if __name__ == "__main__":
    assert GrandChild.mro() == [
        GrandChild, Child1, Parent1, Child2, Parent2, object
    ]
