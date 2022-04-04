# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:15:12 2019

@author: sofia
"""

class princess():
    """
    This class is used to represent the princess, and it contains the attributes of the position x and y, to represent the position of the princess.
    Since the Princess is static, we do not need to create a method to move her.
    But since the attributes are private, we need to use the special method property, so we are able to use the attributes in the main program.
    """
    def __init__(self,x,y):
        self.__posx=x
        self.__posy=y
    
    @property
    def posx(self):
        return self.__posx
    
    @property
    def posy(self):
        return self.__posy