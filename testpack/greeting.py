# -*- coding: utf-8 -*-

from pkg_resources import resource_string


def say_hello():
    print("Hello!")



def give_quote():
    x = resource_string(__name__, 'wilde.txt').decode().strip()
    print(x)

 