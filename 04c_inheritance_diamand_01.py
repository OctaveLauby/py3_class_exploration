"""
        Parent
        /     \
    /             \
Child1          Child2
    \             /
        \     /
       GrandChild
"""


# ----

class Parent(object):
    def __init__(self):
        print("Parent")
        self.content = "parent"


class Child0(Parent):
    def __init__(self):
        print("Child0")
        super().__init__()


class Child1(Parent):
    def __init__(self):
        print("Child1")
        super().__init__()
        self.content = "child1"


class Child2(Parent):
    def __init__(self):
        print("Child2")
        super().__init__()
        self.content = "child2"


class GrandChild00(Child0, Child1):
    def __init__(self):
        print("GrandChild00")
        super().__init__()


class GrandChild0(Child1, Child2):
    def __init__(self):
        print("GrandChild0")
        super().__init__()


class GrandChild1(Child1, Child2):
    def __init__(self):
        print("GrandChild1")
        super().__init__()
        self.content = "grandchild1"


if __name__ == '__main__':

    print("\nBuilding GrandChild00 object:")
    print("> %s" % GrandChild00.mro())
    grandchild00 = GrandChild00()
    assert grandchild00.content == "child1"

    print("\nBuilding GrandChild0 object:")
    print("> %s" % GrandChild0.mro())
    grandchild0 = GrandChild0()
    assert grandchild0.content == "child1"

    print("\nBuilding GrandChild1 object:")
    print("> %s" % GrandChild1.mro())
    grandchild1 = GrandChild1()
    assert grandchild1.content == "grandchild1"
