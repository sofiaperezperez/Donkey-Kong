# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:06:13 2019

@author: sofia
"""

class stairs:
    """
    This class is used to represent each of the stairs. 
    The attributes that are needed are the x and y coordinates, to represent the location of the objects.
    Since the attributes are private, we need to use the special method property, so we are able to use the attributes in the main program.
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