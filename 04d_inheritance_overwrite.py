"""Here is a way to ease function overwritting without having to rewrite doc.
"""


class OverwrittingError(Exception):
    pass


class A(object):
    def f(self):
        """A function to overwrite that has a docstring."""
        return 1

    @classmethod
    def overwrite(cls, meth):
        try:
            meth.__doc__ = getattr(A, meth.__name__).__doc__
        except AttributeError:
            raise OverwrittingError(
                "%s is not a method of A that can be overwritten"
                % meth.__name__
            )
        return meth


class B(A):
    @A.overwrite
    def f(self):
        return 2


if __name__ == '__main__':
    b = B()
    assert b.f() == 2
    assert b.f.__doc__ == A.f.__doc__

    try:
        class C(A):
            @A.overwrite
            def g(self):
                return 3
    except OverwrittingError:
        pass
    else:
        raise Exception("Should have failed here")