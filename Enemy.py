"""

    Enemy UML 
=================
    var
    ===
 -Health
 
    method
   ======== 
 +StillAlive
 +walk
 +jump
 +sound


Author: Salvador Orozco
Version: 1
Program: Enemy Class
"""

class Enemy:

    def __init__(self):
        #intial health for basic enemy is 100 will override for boss
        self.__Health = 100

        
    #method checks enemy health
    def checkHealth(self):
        if self.__Health <= 0:
            print("Enemy is Dead")
        else:
            print("Life remaining: "+str(self.__Health))

    #methode allows for enemy to walk in game
    def walk(self):
        #need to create enviroment to test
        return 0
    
    #methods allows for enemy to jump
    def jump(self):
        #need to create envirment to test
        return 0
    
    #method creates sound when enemy is dead
    def sound(self):
        #need sound file
        return 0
