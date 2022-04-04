# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:57:08 2019

@author: sofia
"""

import princesa
import donkeykong

WIDTH = 256
HEIGHT = 256
CAPTION = "This is our game!"
marioinitialx=120
marioinitialy=224
princesainitialx=80
princesaintialy=4
princesainitial=princesa.princess(30,59)
donkeykonginitial=donkeykong.donkeykong(3,59)
donkeykonginitialx=10
donkeykonginitialy=30
score=0


"""
This file is called "constantes", and it is used to store important values, such as the initial position of mario, the princess, and DonkeyKong, that will be used in the main program, for example when mario dies, and has to go back to  the initial position.
We have also stored here the total lifes and the total score, both at the beggining of the game.
"""
