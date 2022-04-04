# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:18:14 2019

@author: sofia
"""

class donkeykong():
    """
    This class is used to represent the donkey object, and it contains several attributes such as:
        -The coordinates x and y of the donkey, to represent its location.
        -To make the donkey dinamic, a list of lists os the possible images that can take Donkeykong. To do so, we also need to create an attribute of the index of the list of images.
        """
    def __init__(self,x,y):
        self.__posx=x
        self.__posy=y
        self.__images=[[104,58],[150,58]]
        self.__indeximages=0

    """
      Since our attributes are private, we need to use the special method property so we are able to use these attributes in our main program.

"""


    @property
    def posy(self):
        return self.__posy

    @property
    def posx(self):
        return self.__posx

    @property
    def images(self):
        return self.__images

    @property
    def indeximages(self):
        return self.__indeximages

    def moves(self):
        self.__indeximages=(self.__indeximages+1)%len(self.images)

        """
        This method is used to change the value of the index, in order to change the images of the object.
        """


    def getimagen(self):
        """
        This method is used to select an image of the object, depending on the value of the index.
        We also divide by the length of each of the lists in order to never obtain one index higher than the total of elements that belong to that list.
        """
        self.__coord=self.__images[(self.__indeximages)%len(self.__images)]
        return self.__coord




