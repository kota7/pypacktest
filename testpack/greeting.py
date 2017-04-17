# -*- coding: utf-8 -*-

from pkg_resources import resource_string


def say_hello():
    """
    Print 'Hello!' on concole
    
    :return: None
    """
    print("Hello!")



def give_quote():
    """
    Print a nice quote by Oscar Wilde
    
    :return: None
    """ 
    x = resource_string(__name__, 'wilde.txt').decode().strip()
    print(x)

 