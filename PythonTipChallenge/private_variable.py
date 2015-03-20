# -*- coding: utf-8 -*-


class Foo(object):

    def __init__(self):
        self._a = 'a'
        self.__b = 'b'


class Boo(Foo):

    def __init__(self):
        super(Boo, self).__init__()


f = Foo()
print(f._a)

b = Boo()
print(b._a)

print(f._Foo__b)
