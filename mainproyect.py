# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:26:12 2019

@author: sofia
"""
"""
We need to import all the files with the classes that we are going to use in this program, taking into account that all of them must be in the same folder.
"""
import pyxel

import constantes

import mario

import princesa

import donkeykong

import escaleras

import plataformas

import barril

import random

class Game():

    """
    Our game is going to be implemented in one class, the Game class, and we are going to set the attributes, that correspond to the characters of the game:
    -The princess, that is and object of the princess class, in which we have to introduce her initial position,that is going to be taken from constantes.
    -Mario, that is an object of the Mario class, and we need to introduce his initial position, that is going to be taken from constantes.
    -DonkeyKong, that is an object of the DOnkeyKong class, and we also need to introduce the initial position, that is also going to be taken from constantes.
    -We create a list called "stairs", in which we are going to store all the stairs objects created from the stairs class. We created them using a range and just changing the y value..
    -We have also created a list called "deco stairs" in which we are going to store the stairs that we are not going to use, but the are decoration.
    -At the end we did the same thing with the platforms, created a list in which we stored all the objects of the class platforms, that we created using a range and just changing the x value.
    """




    def __init__(self):

        self.princessobj=princesa.princess(constantes.princesainitialx,constantes.princesaintialy)

        self.marioobj=mario.Mario(constantes.marioinitialx,constantes.marioinitialy)

        self.donkeykongobj=donkeykong.donkeykong(constantes.donkeykonginitialx,constantes.donkeykonginitialy)

        self.stairs=[]
        self.stairsdeco=[]
        self.barrel=[]

        for i in range(7):

            stairsobj=escaleras.stairs(190,234-6*i)

            self.stairs.append(stairsobj)

        for i in range(7):

            stairsobj=escaleras.stairs(50,176-6*i)

            self.stairs.append(stairsobj)

        for i in range(8):

            stairsobj=escaleras.stairs(170,118-6*i)

            self.stairs.append(stairsobj)


        for i in range(3):

            stairsobj=escaleras.stairs(25,234-6*i)
            self.stairsdeco.append(stairsobj)



        for i in range(14):

            stairsobj=escaleras.stairs(62,54-6*i)

            self.stairsdeco.append(stairsobj)



        for i in range(14):

            stairsobj=escaleras.stairs(52,54-6*i)

            self.stairs.append(stairsobj)



        for i in range(3):

            stairsobj=escaleras.stairs(126,54-6*i)

            self.stairs.append(stairsobj)



        self.plataforms=[]

        for i in range(29):

            platformssobj=plataformas.platforms(i*8,60)

            self.plataforms.append(platformssobj)

        for i in range(32):

            platformssobj=plataformas.platforms(i*8+20,124)

            self.plataforms.append(platformssobj)

        for i in range(28):

            platformssobj=plataformas.platforms(i*8,182)

            self.plataforms.append(platformssobj)

        for i in range(31):

            platformssobj=plataformas.platforms(i*8,240)

            self.plataforms.append(platformssobj)

        for i in range(8):

            platformsobj=plataformas.platforms(i*8+71,26)

            self.plataforms.append(platformsobj)


        pyxel.init(constantes.WIDTH, constantes.HEIGHT, caption=constantes.CAPTION)
        """
        We create the screen, using the values of width and height stored in constantes.
        We also load the file in which the images that we will use to represent each object are.
        """

        pyxel.load("assets/my_resource.pyxres")


        """
        In order to introduce sound to our game we used the sound.set() function which is used to create sounds from                            strings. After, we stablished an attribute play_music with a boolean value = True.
        """

        pyxel.sound(0).set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )

        pyxel.sound(1).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )

        pyxel.sound(2).set(
            "c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )

        pyxel.sound(3).set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )

        pyxel.sound(4).set(
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25
        )

        self.play_music(True, True, True)

        pyxel.run(self.update, self.draw)  #also we run the two main methods of the class, update and draw.

    def play_music(self, ch0, ch1, ch2):

        #Finally, implementing a play_music function we could get the sounds in our game.

        pyxel.play(0, [0, 1], loop=True)
        pyxel.play(1, [2, 3], loop=True)
        pyxel.play(2, 4, loop=True)

    def existPlatformForMario(self,coordX,coordY):
        """
        This method is used to check if Mario is on a platform or if it is not. We do it by approximating the x and y coordinates of the mario object, and checking if it coincides with the ones of each of the platforms. If true or false is returned, it means that mario is or is not on a platform, respectively.
        """
        for i in self.plataforms:
            #Counting from down to up
            #It falls from the second platform
            if coordX>218:
                if coordY<224 and coordY >165:
                    return False
                #It falls from the fourth one
                elif coordX> 224 and coordY<108:
                    return False

            #It falls from the third one
            elif coordX<13:
                if coordY<166 and coordY>60:
                    return False


            #It falls from the fifth one
            elif coordX>135-8 and coordX<135:
                if coordY<44:
                    return False

        return True

    def existPlatformForBarrel(self,coordX,coordY):
        """
        This method is used to check if the each of the objects barrels are o are not on a platform.
         We do it by approximating the x and y coordinates of each of the barrels objects, and checking if they coincide with the ones of each of the platforms. If true or false is returned, it means that the barrel is or is not on a platform, respectively.
        """

        for i in self.plataforms:
            #Counting from down to up
            #it falls from the first platform
            if coordX<15:
                if coordY<266 and coordY > 182:
                    return False

            #It falls from the second platform
            elif coordX>218:
                if coordY<234 and coordY >165:
                    return False

            #It falls from the third platform
            if coordX<13:
                if coordY<172 and coordY>60:
                    return False

            #It falls from the fourth platform
            elif coordX> 224 and coordY<118:
                return False

        return True

    def existStairForBarrel (self,coordX,coordY):
        """
        This method is used to check if there each of the barrels are on the position of the stairs or not.
        This is done by approximating the coordinates of the barrels with the ones of the stairs. If false or true is returned, it means that the barrel is or is not on a stair, respectively.
        """
        for i in self.plataforms:
            #Counting from up to down
            #It falls from the first stair
            if coordX>161 and coordX<170:

                if coordY<114:
                    return False

            #It falls from the second stair
            elif coordX>46 and coordX<56:

                if coordY<172 and coordY>60:
                    return False

            #It falls from the third stair
            elif coordX>182 and coordX<190:

                 if coordY<230 and coordY >165:

                     return False

        return True


    def update(self):
        """
        This method is used to update all the objects and the whole game every frame, changin the position of some objects, or simulate movement.
        """
        if not self.existPlatformForMario(self.marioobj.posX,self.marioobj.posY):  #if mario is not on a platform, he falls until the next one appears.

            self.marioobj.move(self.marioobj.posX,self.marioobj.posY+1)


        for i in self.barrel:
            pr=random.randint(1,4)
            if pr==1:
                if not self.existStairForBarrel(i.posx,i.posy):
                    i.move(i.posx,i.posy+2)
            # for each of the platforms, if they are on a stairs, they have 25% chances of going down through it, until the barrels reach the next paltform.

            else:
                if not self.existPlatformForBarrel(i.posx,i.posy):  #if it is not on a stair or on a platform, the barrel falls until the next platform appears.
                    i.move(i.posx,i.posy+1)



        if pyxel.frame_count%7==0:
            self.donkeykongobj.moves()
        #every 7 frames, we apply the donkeykong method moves, that changes the index of the list of images.

        if len(self.barrel)<10 and pyxel.frame_count%100==0:   #if the lenght of the list of barrels is less than 10, every 100 frames we are going to create a barrel object, and its initial position is the ones of donkey kong.
           barrelobj=barril.Barril(self.donkeykongobj.posx,self.donkeykongobj.posy+20)
           self.barrel.append(barrelobj)

        for i in self.barrel:
             if i.posx<constantes.WIDTH-256 or i.posy>constantes.HEIGHT:
                 self.barrel.remove(i)
        #If one of the barrels goes off the screen, it is automatically deleted of the list, making space for another barrel.


        if pyxel.btnp(pyxel.KEY_Q):  #if Q is pressed, we close the game.
            pyxel.quit()



        #to move mario left and right,up and down
        elif pyxel.btn(pyxel.KEY_RIGHT):

           """
        To move right, we just make sure that mario is on the screen, and then we move mario increasing the current value of the position x on one.
        Since the movement of the barrels must be autonomic, we needed to implemente it on every botton we pressed, because if we do not do it, when we pressed the bottom, they would stop moving.
           """
           for i in self.plataforms:
               if self.marioobj.posX<256-16:   #first we check that mario is on a platform, and the we use the function move.
                   if self.marioobj.posY+16>=i.posy-2 and self.marioobj.posY+16<=i.posy+2:

                        self.marioobj.move(self.marioobj.posX+0.10,self.marioobj.posY)


           if len(self.barrel)>0:  #we just check if there are at least one barrel, and depending on which platform they are on, they move to the right (increasing the value of the current x plus 0.5) or to the left (decreasing the current value of x minus 0.5)

                for i in self.barrel:

                    for e in self.plataforms:

                            if i.posy+10<=60+2 and i.posy+10>=60-2:

                                if e.posy<=60+2 and e.posy>=60-2:

                                            i.move(i.posx+0.05,i.posy)

                            elif i.posy+10<=182+2 and i.posy+10>=182-2:

                                if e.posy<=182+2 and e.posy>=182-2:
                                            i.move(i.posx+0.05,i.posy)

                            elif i.posy+10<=124+2 and i.posy+10>=124-2:

                                if e.posy<=124+2 and e.posy>=124-2:
                                            i.move(i.posx-0.05,i.posy)

                            elif i.posy+10<=240+2 and i.posy+10>=240-2:

                                if e.posy<=240+2 and e.posy>=240-2:
                                            i.move(i.posx-0.05,i.posy)


        elif pyxel.btn(pyxel.KEY_LEFT):  #to move mario to the left, we do the same as we did to move him to the right, but instead of add one, we decrease one on the value of the x position.

            for i in self.plataforms:

                if self.marioobj.posX>0.10:  #first we check that mario is on a platform, and the we use the function move.

                    if self.marioobj.posY+16>=i.posy-2 and self.marioobj.posY+16<=i.posy+2:

                            self.marioobj.move(self.marioobj.posX-0.10,self.marioobj.posY)




            if len(self.barrel)>0:  #we implement the movement of the barrels

                for i in self.barrel:

                    for e in self.plataforms:

                            if i.posy+10<=60+2 and i.posy+10>=60-2:

                                if e.posy<=60+2 and e.posy>=60-2:

                                            i.move(i.posx+0.05,i.posy)

                            elif i.posy+10<=182+2 and i.posy+10>=182-2:

                                if e.posy<=182+2 and e.posy>=182-2:
                                            i.move(i.posx+0.05,i.posy)

                            elif i.posy+10<=124+2 and i.posy+10>=124-2:

                                if e.posy<=124+2 and e.posy>=124-2:
                                            i.move(i.posx-0.05,i.posy)

                            elif i.posy+10<=240+2 and i.posy+10>=240-2:

                                if e.posy<=240+2 and e.posy>=240-2:
                                            i.move(i.posx-0.05,i.posy)

        elif pyxel.btn(pyxel.KEY_UP):  #to move mario up


            for i in self.stairs:  #first we need to make sure mario is on a stair, and we do it by approximating the possible values of the x and y coordinates of mario, and we compare them with the ones of the stairs.

                if self.marioobj.posX <= i.posx+5 and self.marioobj.posX >= i.posx-5:

                    if self.marioobj.posY <= i.posy+31 and self.marioobj.posY >= i.posy-31:

                        self.marioobj.move(self.marioobj.posX,self.marioobj.posY-1)  #To make mario go up, we  decrease the y coordinate minus one.

            if len(self.barrel)>0:  #to make sure the barrels will not stop, we inplement their movement also when we press the up bottom.

                for i in self.barrel:

                    for e in self.plataforms:

                            if i.posy+10<=60+2 and i.posy+10>=60-2:

                                if e.posy<=60+2 and e.posy>=60-2:

                                            i.move(i.posx+0.05,i.posy)

                            elif i.posy+10<=182+2 and i.posy+10>=182-2:

                                if e.posy<=182+2 and e.posy>=182-2:
                                            i.move(i.posx+0.05,i.posy)

                            elif i.posy+10<=124+2 and i.posy+10>=124-2:

                                if e.posy<=124+2 and e.posy>=124-2:
                                            i.move(i.posx-0.05,i.posy)

                            elif i.posy+10<=240+2 and i.posy+10>=240-2:

                                if e.posy<=240+2 and e.posy>=240-2:
                                            i.move(i.posx-0.05,i.posy)




        elif pyxel.btn(pyxel.KEY_DOWN):  #make mario go down

            for i in self.stairs:   #first we need to make sure mario is on a stair, and we do it by approximating the possible values of the x and y coordinates of mario, and we compare them with the ones of the stairs.

                 if self.marioobj.posY +32 <= i.posy+22 and self.marioobj.posY+32 >= i.posy-22:

                      if self.marioobj.posX <= i.posx+5 and self.marioobj.posX >= i.posx-5:

                          self.marioobj.move(self.marioobj.posX,self.marioobj.posY+1)  #To make mario go down, we increase the y coordinate plus one.


            if len(self.barrel)>0:    #to make sure the barrels will not stop, we inplement their movement also when we press the up bottom.


                for i in self.barrel:

                    for e in self.plataforms:

                            if i.posy+10<=60+2 and i.posy+10>=60-2:

                                if e.posy<=60+2 and e.posy>=60-2:

                                            i.move(i.posx+0.05,i.posy)

                            elif i.posy+10<=182+2 and i.posy+10>=182-2:

                                if e.posy<=182+2 and e.posy>=182-2:
                                            i.move(i.posx+0.05,i.posy)

                            elif i.posy+10<=124+2 and i.posy+10>=124-2:

                                if e.posy<=124+2 and e.posy>=124-2:
                                            i.move(i.posx-0.05,i.posy)

                            elif i.posy+10<=240+2 and i.posy+10>=240-2:

                                if e.posy<=240+2 and e.posy>=240-2:
                                            i.move(i.posx-0.05,i.posy)




      #barrels

        elif len(self.barrel)>0:   #here we implement the movement of the barrels, if it is no pressed any bottom. we just check if there are at least one barrel, and depending on which platform they are on, they move to the right (increasing the value of the current x plus 0.5) or to the left (decreasing the current value of x minus 0.5)

            for i in self.barrel:

                for e in self.plataforms:

                        if i.posy+10<=60+2 and i.posy+10>=60-2:

                            if e.posy<=60+2 and e.posy>=60-2:

                                        i.move(i.posx+0.05,i.posy)

                        elif i.posy+10<=182+2 and i.posy+10>=182-2:

                            if e.posy<=182+2 and e.posy>=182-2:
                                        i.move(i.posx+0.05,i.posy)

                        elif i.posy+10<=124+2 and i.posy+10>=124-2:

                            if e.posy<=124+2 and e.posy>=124-2:
                                        i.move(i.posx-0.05,i.posy)

                        elif i.posy+10<=240+2 and i.posy+10>=240-2:

                            if e.posy<=240+2 and e.posy>=240-2:
                                        i.move(i.posx-0.05,i.posy)


        if pyxel.btnp(pyxel.KEY_SPACE):  #this makes mario jump
            for e in self.plataforms:  #first we check  that mario is over a platform and then we use the function jump, making him move increasing the x coordinate with 20.
                if self.marioobj.posY+16<=60+2 and self.marioobj.posY+16>=60-2:
                    if e.posy<=60+2 and e.posy>=60-2:
                        self.marioobj.jump(20)

                        self.marioobj.timejumpingchange=pyxel.frame_count

                        self.marioobj.jumpingchange=True


                elif self.marioobj.posY+16<=182+2 and self.marioobj.posY+16>=182-2:

                    if e.posy<=182+2 and e.posy>=182-2:
                        self.marioobj.jump(20)
                        self.marioobj.timejumpingchange=pyxel.frame_count

                        self.marioobj.jumpingchange=True

                elif self.marioobj.posY+16<=124+2 and self.marioobj.posY+16>=124-2:
                    if e.posy<=124+2 and e.posy>=124-2:
                        self.marioobj.jump(20)
                        self.marioobj.timejumpingchange=pyxel.frame_count

                        self.marioobj.jumpingchange=True
                elif self.marioobj.posY+16<=240+2 and self.marioobj.posY+16>=240-2:
                    if e.posy<=240+2 and e.posy>=240-2:
                        self.marioobj.jump(20)

                        self.marioobj.timejumpingchange=pyxel.frame_count

                        self.marioobj.jumpingchange=True




        elif (self.marioobj.jumpingchange and pyxel.frame_count-self.marioobj.timejumping==5):
            self.marioobj.desjump(15)  #if mario is jumping, and he has been doing it for 5 frames, he goes back to the ground.
            for i in self.barrel:
                if i.posy+10>= self.marioobj.posY+16-2 and i.posy+10-2<=self.marioobj.posY+16:  #we compare the position of mario with the barrels.
                    if i.posx> self.marioobj.posX:
                        if i.posx<= self.marioobj.posX+15+12+4:
                            self.marioobj.gainpoints() #if mario jumped over a barrel, we wins 100 points.
                    if i.posx< self.marioobj.posX:
                        if i.posx+12+15+4>= self.marioobj.posX:
                            self.marioobj.gainpoints()  #if mario jumps over a barrel, he gains 100 points.



            self.marioobj.jumpingchange=False

        if not self.marioobj.jumpingchange:  #here we make sure that if mario touches one barrel, he loses a life and starts in the begining positon.
            for i in self.barrel:
                if i.posy+10+2>self.marioobj.posY+16 and i.posy+10-2<self.marioobj.posY+16: #here we make sure mario is touching a barrel, and we do it approximating the x and y  barrel position, and comparing them to the ones of mario.
                    if i.posx+1>self.marioobj.posX+16 and i.posx-2<self.marioobj.posX+15:
                        self.marioobj.move(constantes.marioinitialx,constantes.marioinitialy)  #mario goes back to the begining position
                        self.marioobj.loselife()
                    if i.posx+10<self.marioobj.posX and i.posx+10>self.marioobj.posX-2:
                        self.marioobj.move(constantes.marioinitialx,constantes.marioinitialy)
                        self.marioobj.loselife()  #mario loses a life
                    #if a barrel is going down a ladder and Mario is in it, Mario will lose a life

                else:
                    for o in self.stairs:
                        if i.posx <= o.posx+5 and i.posx >= o.posx-5:
                            if i.posy <= o.posy+31 and i.posy >= o.posy-31:
                                if self.marioobj.posX <= o.posx+5 and self.marioobj.posX >= o.posx-5:
                                    if self.marioobj.posY <= o.posy+31 and self.marioobj.posY >= o.posy-31:
                                        if i.posy+10+2== self.marioobj.posY:
                                            self.marioobj.move(constantes.marioinitialx,constantes.marioinitialy)
                                            self.marioobj.loselife()



        if self.marioobj.totallifes==0:  #if mario runs out of lifes, the game ends.
             pyxel.quit()


    def draw(self):

        #This method is used to create the screen, with all our objects and the decorations


        pyxel.cls(0)  #we created the screen black


        #plataformas

        for i in self.plataforms:

            pyxel.blt(i.posx,i.posy,0,0,0,8,16,colkey=0)   #we create the platforms, using the folder of images that we loaded at the begining.

        #escaleras

        for i in self.stairs:

            pyxel.blt(i.posx,i.posy,0,0,18,8,6,colkey=0)  #every object in the stair list is going to be represented in the screen.

        for i in self.stairsdeco:
            pyxel.blt(i.posx,i.posy,0,0,18,8,6,colkey=0)    #every object in the stair deco list is going to be represented in the screen.

        #princesa

        pyxel.blt(self.princessobj.posx,self.princessobj.posy,0,6,178,18,22,colkey=0) #here we draw the princess.



        #mono
        self.coord=self.donkeykongobj.getimagen() #to simulate the movement, we change the images every frame
        pyxel.blt(self.donkeykongobj.posx,self.donkeykongobj.posy,0,self.coord[0],self.coord[1],39,31,colkey=0)



        #mario
        if pyxel.frame_count%5==0:
            self.coord1=self.marioobj.getimagen()   #every 5 frames we change the image of mario
        pyxel.blt(self.marioobj.posX,self.marioobj.posY,0,self.coord1[0],self.coord1[1],15,16,colkey=0)


        #barels
        for i in self.barrel:
            if pyxel.frame_count%5==0:
                self.coord2= i.getimage  #every 5 frames we change the image of the barrels
            pyxel.blt(i.posx,i.posy,0,self.coord2[0],self.coord2[1],12,10,colkey=0)


        #lives and decorations
        for i in range(self.marioobj.totallifes):
            pyxel.blt(220+10*i,7,0,130,8,8,7,colkey=0)


        #blue thing

        for i in range(3):

            pyxel.blt(2,232-8*i,0,8,8,16,8,colkey=0)

        #heart
        if self.marioobj.posX!=constantes.princesainitialx and self.marioobj.posY>= constantes.princesaintialy+25: #if mario has not reached the princess, she has her heart broken
            pyxel.blt(constantes.princesainitialx+20,constantes.princesaintialy,0,214,180,16,13,colkey=0)
        else:
            pyxel.blt(constantes.princesainitialx+20,constantes.princesaintialy,0,190,180,16,13,colkey=0)
            #if they are together, the princess is not sad anymore! Game over, mario won.







        #fire

        pyxel.blt(4,208,0,24,8,16,8)

        pyxel.text(215,20,"HIGH SCORE",15)
        pyxel.text(227,30,str(self.marioobj.totalpoints),15)  #the score is going to increase and the total is going to be shown in the screen.


    ################## main program ##################


Game()  #we call the class game and we run it.

