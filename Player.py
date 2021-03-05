import pygame


#PLAYER CLASS
class Player:

    #(object, screen to draw on, image of the player, X coord to place image, Y coord to place image)
    def __init__(self, gameScreen, PlayerRight, PlayerLeft, X, Y):

        #Get the game sceen
        self.screen = gameScreen
        #get attributes of the screen
        self.screenInfo = pygame.display.Info()
        self.screen_h = self.screenInfo.current_h
        self.screen_w = self.screenInfo.current_w
        #print screen object attributes
        print(self.screen_h)
        print(self.screen_w)

        #Player Images
        #===================================================================================
        #index and counter for player animation
        self.index = 0
        self.counter = 0

        #how fast the list is iterated for player images
        self.animeSpeed = 2

        #keeps track of the direciton
        self.animeDirection = 0

        #right and left direction image lists
        self.PlayerR = PlayerRight
        self.PlayerL = PlayerLeft

        #image used for the player
        self.player_img = self.PlayerR[self.index]

        #create a rectangle out of the player
        self.rect = self.player_img.get_rect()

        #initial cooridnates to draw player on to screen
        self.rect.x = X
        self.rect.y = Y

        #width and hight of the images
        self.width = self.player_img.get_width()
        self.height = self.player_img.get_height()
        #====================================================================================

        #var used for player jump speed
        self.jump = 0

        #screen.blit("player img goes here" (x, y))
        self.__setHealth = 3

    #get player x coord
    def get_PlayerX(self):
        return (self.rect.x)

    #get player Y Coord
    def get_PlayerY(self):
        return (self.rect.y)

    def Player_Right(self):
        if self.rect.right > self.screen_w:
            self.rect.right = self.screen_w
        self.rect.x += 15
        #counter used for animation
        self.counter += 1
        #Set the direction the image is walking
        self.animeDirection = 1

    def Player_Left(self):
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x -= 15
        #counter used for animation
        self.counter += 1
        #Set the direction the image is walking
        self.animeDirection = -1

    def Player_Jump(self):
        #JUMP NEEDS WORK
        self.jump = -20
        self.rect.y += self.jump

        print("Player Y: " + str(self.rect.y) + "Jump height: " +
              str(self.jump))

    def Player_Gravity(self):

        #Boundries
        #==================================================================
        #Stops player from falling off the screen
        if self.rect.bottom >= self.screen_h:
            self.rect.bottom = self.screen_h
        #Stops player from jumping off screen
        if self.rect.top < 0:
            self.rect.top = 0


#==================================================================

#Gravity pull
        self.jump += 1
        if self.jump > 10:
            self.jump = 10
        self.rect.y += self.jump

    #draw player on screen
    def draw(self):

        #handle animation steps
        if self.counter > self.animeSpeed:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.PlayerR):
                self.index = 0
            if self.animeDirection == 1:
                self.player_img = self.PlayerR[self.index]
                print("Player Direction X: " + str(self.animeDirection) +
                      " PlayerR Index: " + str(self.index) +
                      " PlayerR Counter: " + str(self.counter))
            if self.animeDirection == -1:
                self.player_img = self.PlayerL[self.index]
                print("Player Direction X: " + str(self.animeDirection) +
                      " PlayerL Index: " + str(self.index) +
                      " PlayerL Counter: " + str(self.counter))

        #draws image
        self.screen.blit(self.player_img, self.rect)
        #temp draw rectangle
        #pygame.draw.rect(self.screen,(255,255,255),self.rect,5)
