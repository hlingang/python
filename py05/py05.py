#!/usr/bin/python
'''
装饰器对象:
以被装饰函数为入参, 返回一个代理函数的可调用对象
1. 直接定义的函数
2. 由接实例化的可调用对象
3. 由函数调用返回的可调用对象
'''


def decorator(index=1):

    def _decorator(func):

        def wrap(*args, **kwargs):
            print("decorate-index:", index)
            return func(*args, **kwargs)

        return wrap

    return _decorator


class Decorator(object):

    def __init__(self, index=0):
        self.index = index

    def __call__(self, func):

        def wrap(*args, **kwargs):
            print("Decorator-index:", self.index)
            return func(*args, **kwargs)

        return wrap


@decorator(index=10)
def test01():
    print("test001")


@Decorator(index=11)
def test02():
    print("test001")


if __name__ == "__main__":
    test01()
    test02()
