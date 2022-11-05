#!/usr/bin/python
'''
python 多级继承
子类对象中包含的信息
父类中的所有属性都会被完全覆盖(只保留一份属性数据,不保留父类属性的副本)
子类会保留父类所有方法的副本
'''


class A(object):
    ID = 1

    def __init__(self):
        self.a = 10

    def test(self):
        print("A test(ID:%d) - %d" % (self.__class__.ID, self.a))


class B(A):
    ID = 2

    def __init__(self):
        super().__init__()
        self.a = 20

    def test(self):
        print("B test(ID:%d) - %d" % (self.__class__.ID, self.a))


class C(B):
    ID = 3

    def __init__(self):
        super().__init__()
        self.a = 30

    def test(self):
        print("C test(ID:%d) - %d" % (self.__class__.ID, self.a))


if __name__ == "__main__":
    c = C()
    c.test()
    super(C, c).test()
    super(B, c).test()
