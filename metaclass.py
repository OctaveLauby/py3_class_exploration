class MyMeta(type):

    def __new__(mcs, clsname, superclasses, attributedict):
        print('-----------------------------------')
        print("Allocating memory for class", clsname)
        print(mcs)
        print(superclasses)
        print(attributedict)
        return type.__new__(mcs, clsname, superclasses, attributedict)

    def __init__(cls, clsname, superclasses, attributedict):
        print('-----------------------------------')
        print("Initializing class", clsname)
        print(cls)
        print(clsname)
        print(superclasses)
        print(attributedict)
        super(MyMeta, cls).__init__(clsname, superclasses, attributedict)


class MyKlass(object, metaclass=MyMeta):

    def foo(self, param):
        pass

    barattr = 2


MyKlass()
