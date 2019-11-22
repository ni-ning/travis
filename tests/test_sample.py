# -*- coding:utf-8 -*-


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_environ():
    import os
    print(os.environ)
    print(os.environ['NAME'])
    assert True
