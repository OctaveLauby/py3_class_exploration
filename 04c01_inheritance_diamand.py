"""
        Parent
        /     \
    /             \
Child1          Child2
    \             /
        \     /
       GrandChild
"""

# --------------------------------------------------------------------------- #
# ---- All inits are overwritten

class Parent(object):
    def __init__(self):
        print("Parent")
        self.content = "parent"


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


class GrandChild(Child1, Child2):
    def __init__(self):
        print("GrandChild")
        super().__init__()
        self.content = "grandchild"


if __name__ == '__main__':

    print("\nBuilding GrandChild object:")
    assert GrandChild.mro() == [GrandChild, Child1, Child2, Parent, object]
    instance = GrandChild()
    assert instance.content == "grandchild"


# --------------------------------------------------------------------------- #
# ---- GrandChild init not overwritten

class Parent(object):
    def __init__(self):
        self.content = "parent"


class Child1(Parent):
    def __init__(self):
        super().__init__()
        self.content = "child1"


class Child2(Parent):
    def __init__(self):
        super().__init__()
        self.content = "child2"


class GrandChild(Child1, Child2):
    def __init__(self):
        print("GrandChild")
        super().__init__()


if __name__ == '__main__':
    instance = GrandChild()
    assert instance.content == "child1"


# --------------------------------------------------------------------------- #
# ---- Child init args != from parent init args

# -- Issue :

class Parent(object):
    def __init__(self, n):
        self.n = n
        self.content = "parent"


class Child1(Parent):
    def __init__(self):
        super().__init__(n=1)
        self.content = "child1"


class Child2(Parent):
    def __init__(self):
        super().__init__(n=2)
        self.content = "child2"


class GrandChild(Child1, Child2):
    def __init__(self):
        super().__init__()
        self.content = "grandchild"


if __name__ == '__main__':
    try:
        instance = GrandChild()
    except TypeError:
        pass
    else:
        raise Exception("Should have failed")


# -- Solution :
# method :not using supe
# benefits :
#     - light syntax
#     - good and clear control on arguments
# objections :
#     - Parent __init__ is called twice

class Parent(object):
    def __init__(self, n):
        self.n = n
        self.content = "parent"


class Child1(Parent):
    def __init__(self):
        Parent.__init__(self, n=1)
        self.content = "child1"
        self.is_child1 = True


class Child2(Parent):
    def __init__(self):
        Parent.__init__(self, n=2)
        self.content = "child2"
        self.is_child2 = True


class GrandChild(Child1, Child2):
    def __init__(self):
        Child1.__init__(self)
        Child2.__init__(self)
        self.content = "grandchild"


if __name__ == '__main__':
    instance = GrandChild()
    assert instance.content == "grandchild"
    assert instance.n == 2
    assert instance.is_child1
    assert instance.is_child2


# -- Solution :
# method : using super
# benefits :
#     - parent __init__ called once
# objections :
#     - Unclear use of *args and **kwargs
#       > (someone not knowing diamand inheritance won't understand)
#     - risk of untracked error (wrong args used when calling childs)


class Parent(object):
    def __init__(self, n):
        self.n = n
        self.content = "parent"


class Child1(Parent):
    def __init__(self, *args, **kwargs):
        super().__init__(n=1)
        self.content = "child1"
        self.is_child1 = True


class Child2(Parent):
    def __init__(self, *args, **kwargs):
        super().__init__(n=2)
        self.content = "child2"
        self.is_child2 = True


class GrandChild(Child1, Child2):
    def __init__(self):
        super().__init__()
        self.content = "grandchild"


if __name__ == '__main__':
    instance = GrandChild()
    assert instance.content == "grandchild"
    assert instance.n == 2
    assert instance.is_child1
    assert instance.is_child2
