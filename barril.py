# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:09:51 2019

@author: sofia
"""

class Barril:
    """
    This class is used to represent each of the barrels.
    The attributes are:
        -The position of each of the barrels, with the x and y coordinates.
        -We also create a list of lists of eaach of the images of the barrels that are going to be changing every 7 frames, and to do that we have also created the attribute index.
    """
    def __init__(self,x,y):
        self.__posx=x
        self.__posy=y
        self.__image=[[35,105],[59,105],[82,105],[107,105]]
        self.__index=0


    def move(self,value,valuetwo):
        """
        This method is going to be used for changing the position of each of the barrels, and it has two parameters that need to be inserted, and are the new position of the barrels.
        We have also used this method to change the value of the attribute index, so every time the barrel moves, it changes of image.We also divide by the length of each of the lists in order to never obtain one index higher than the total of elements that belong to that list.
        """
        self.__posx=value
        self.__posy=valuetwo
        self.__index=(self.__index+1)%len(self.__image)
        return self.__posx and self.__posy

    @property
    def getimage(self):
        self.__coord=self.__image[self.__index]
        return self.__coord

    @property
    def posx(self):
        return self.__posx

    @property
    def index(self):
        return self.__index

    @property
    def posy(self):
        return self.__posy

    """
    Since our attributes are private, we need the method property to be able to use the attribute coord in our main program. We also need to do this in the attributes of the position x and y, and the index.
    """
