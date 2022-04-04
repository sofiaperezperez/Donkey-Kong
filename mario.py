# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:26:12 2019

@author: sofia
"""
#import random

class Mario:
    """
    This class represents the character Mario or the player, and contains all the methods related to it.
    The attirbutes that are in this class are:
        -The position of mario, with the x and y coordinates.
        -Jumping and Desumping to show if mario is jumping or if it is not.
        -To do a dinamic Mario, we have created a list of lists containing all the images that we want to be chaging, in order to simulate movement. Depending on if Mario is going to the right, left, or up and down, we have created different lists.
        -To complete that task we needed to create also the indexes that are going to be changing in order to  be changing of images.
        -The attirbute direccion refers to the direction that takes mario, depending on if he is walking to the right side, the left, up or down.
        -The other attribute is the remain number of lifes, and in the start it starts with three lifes.
        -The last attributed we have created is the total points, that starts in zero, and is going to be increasing.
    """

    def __init__(self,x,y):
        self.__posX=x
        self.__posY=y
        self.__jumping=False
        self.__desjumping=False
        self.__timejumping=0
        self.__direccion="derecha"
        self.__imagenesi=[[5,32],[29,32],[53,32]]
        self.__imagenesd=[[5,32],[29,32],[53,32]]
        self.__imagenesup=[[78,32],[101,32]]
        self.__indexd=0
        self.__indexi=0
        self.__indexup=0
        self.__indexnormal=0
        self.__totallifes=3
        self.__totalpoints=0



    def move(self,value,valuetwo):
        """
        This method is used to move mario, and we need to insert two parameters, the new position of mario, with the coordinates x and y.
        It is also used to determine the direction that mario takes, depedning on if the new value of x is higher lower than the previous one, and if the new value of y is lower or higher then the previous one.
        Depending on the direccion the mario takes in each moment, the corresponded index is going to increase. We also divide by the length of each of the lists in order to never obtain one index higher than the total of elements that belong to that list.

        """

        if value> self.posX:
            self.__indexd=(self.__indexd+1)%len(self.__imagenesd)
            self.__direccion="derecha"

        elif value<self.posX:
            self.__direccion="izquierda"
            self.__indexi=(self.__indexi+1)%len(self.__imagenesi)
        else:
            self.__direccion="up"
            self.__indexup=(self.__indexup+1)%len(self.__imagenesup)

        self.__posX=value
        self.__posY=valuetwo
        return self.__posX and self.__posY

    @property
    def direccion(self):
        return self.__direccion

    @property
    def imagenesd(self):
        return self.__imagenesd

    @property
    def imagenesup(self):
        return self.__imagenesup
    @property
    def indexd(self):
        return self.__indexd

    @property
    def indexi(self):
        return self.__indexi

    @property
    def indexup(self):
        return self._indexup

    """
    Since our attributes are private, we need the method property to be able to use them in the main program.
    If we wanted to change the values of the private attributes in the main program, we would have needed a setter method, but since we change its vallue in the same class, it is not needed, and just works as a normal method.
    """

    def indexdchange(self,value):
        self.__indexd=value
        return self.__indexd


    def indexupchange(self,value):
        self.__indexup=value
        return self.__indexup

    @property
    def posX(self):
        return self.__posX
    @property
    def desjumping(self):
        return self.__desjumping

    @property
    def jumping(self):
        return self.__jumping

    @jumping.setter
    def jumpingchange(self,value):
        self.__jumping=value

    @property
    def timejumping(self):
        return self.__timejumping

    @timejumping.setter
    def timejumpingchange(self,value):
        self.__timejumping=value

    @property
    def posY(self):
        return self.__posY
    @property
    def totallifes(self):
        return self.__totallifes

    @property
    def totalpoints(self):
        return self.__totalpoints

    def loselife(self):
        """
        This method is used to rest a life (Mario starts with 3),when he dies.
        """
        self.__totallifes-=1


    def getimagen(self):
        """
        This method is used to make mario dinamic nd simulate movement. First of all it checks the direccion of mario, and depending on that, and on the value of the corresponded index, it selects an element of the list of images.
        """

        if self.__direccion=="derecha":
            self.coord1=self.__imagenesd[(self.__indexd)%len(self.__imagenesd)]

        if self.__direccion=="izquierda":
            self.coord1=self.__imagenesi[(self.__indexi)%len(self.__imagenesi)]

        if self.__direccion=="up":
            self.coord1=self.__imagenesup[(self.__indexup)%len(self.__imagenesup)]


        return self.coord1


    def jump(self,value):
        """
        This method makes Mario jump, changing the value of the x and y coordinates, and depending on if the direction of mario is right or left, he is going to jump to one side or another, respectively.
        """
        if self.__direccion=="derecha":
            self.__posX+=value
        else:
            self.__posX-=value


        self.__posY-=15
        self.__jumping=True

    def desjump(self,value):
        """
        This method makes mario go back to the ground after having jumped.
        It changes the values of the x and y coordinates.
        the y coordinate changes the as much as it did in the method jump.
        """
        if self.__direccion=="derecha":
            self.__posX+=value
        else:
            self.__posX-=value

        self.__posY+=15
        self.__desjumping=False

    def gainpoints(self):
        """
        This method is used to add 100 points to the attribute totalpoints, and we will use it in the main funcion under the appropiate circumstances.
        """
        self.__totalpoints+=100

