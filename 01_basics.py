"""Basics about python3 class.

Notations:
    cls         current class
    self        current instance


Personal notation:
    instance        a instance of the class


Good use:
    all attributes are define (can be set to None) in __init__
"""


class MyClass(object):
    """Basic class."""

    # ----------------------------------------------------------------------- #
    # Class attributes

    cls_attr = "class attribute"

    # ----------------------------------------------------------------------- #
    # Instance initialisation

    def __init__(self, *args, **kwargs):
        """Called after __new__, initialize instance content.

        Does not return anything
        """
        self.attr = "instance attribute"
        self.history = []

    # ----------------------------------------------------------------------- #
    # Instance methods

    def my_method(self, *args, **kwargs):
        """instance method, can do any thing."""
        self.history.append("my_method")

    # ----------------------------------------------------------------------- #
    # Special methods:
    # # called when using specific syntaxew
    # # way to allow operations such as: +, *, iter, _[key], ...
    # # @see https://docs.python.org/3/reference/datamodel.html

    def __str__(self):
        """return string of self

        Called in following cases:
            >>> str(instance)
            >>> "%s" % instance
            >>> "{}".format(instance)
            >>> print(instance)
        """
        return "%s(%s)" % (self.__class__.__name__, self.attr)

    def __repr__(self):
        """Return representation of self, usually more explicit than string

        Called in following cases:
            >>> instance
            >>> repr(instance)
            >>> print([instance])
        """
        return "<%s>" % self

    # ----------------------------------------------------------------------- #
    # Class methods

    @classmethod
    def my_cls_method(cls, *args, **kwargs):
        """A class method.

        It is directly related to the class. For instance if you have a class
        Point, you can implement a class method create_random that return a
        random point.
        """
        print("Class method '%s.my_cls_method' called" % cls.__name__)
        return cls

    @staticmethod
    def my_static_method(*args, **kwargs):
        """A static method.

        cls does not appear in arguments, it is called the same way as a class
        method though.
        """
        print("Static method called, defined in %s" % MyClass.__name__)


if __name__ == "__main__":
    instance = MyClass()
    instance.my_method()
    print(instance)
    print(repr(instance))
    print(instance.history)
    MyClass.my_cls_method()
    MyClass.my_static_method()
