class Test():

    def __init__(self, n):
        self.attr1 = n
        self._attr2 = n+1
        self.__attr3 = "1"
        self._dict = {}

    def __radd__(self, n):
        return self.attr1 + n

    @property
    def dic(self):
        return self._dict


class Test2(Test):

    def __init__(self, n):
        super().__init__(n)
        self.attr1 = -5
        self.__attr3 = "2"


t = Test2(1)
assert (t.attr1, t._attr2) == (-5, 2)
t._Test__attr3 = 5
assert t._Test__attr3 == 5
assert t._Test2__attr3 == "2"
assert "Sum:", 1 + t == -4
d = t.dic
d[0] = 1
print(t.dic)
