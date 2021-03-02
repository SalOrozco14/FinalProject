"""

Paige's Completion
==========================
Background - 3/1/2020
Player sprite - 3/1/2020
Friend Sprite - 3/1/2020
New item Laser - 3/1/2020


Jumping Method - In Progess
Player Class - In Progress
Rocketship Sprite - In Progress
Ground Environment - In Progress

"""

#PLAYER CLASS
class Player:

    def __init__(self, X, Y):
        #draws player on to screen
        self.__playerX = X
        self.__playerY = Y

        #screen.blit("player img goes here" (x, y))
        self.__setHealth = 3

        # isJump and jumpCount attributes
        self.isJump = False
        self.jumpCount = 10

    #get player x coord
    def get_PlayerX(self):
        return (self.__playerX)
        
    #get player Y Coord
    def get_PlayerY(self):
        return (self.__playerY)

    #move player right
    def Player_Right(self):
        self.__playerX += 10

    #move player left
    def Player_Left(self):
        self.__playerX -= 10

""""
    def jump(self):
      velx = 10
      vely = 10
      jump = False

      if jump is False and userinput[pygame.K_UP]:
        jump = True

      if jump is True:
        y -= vely
        vely -= 1
      if y < -10:
        jump = False
        vely = 10
        
"""
""""
    def Player_Ground(self):
        return 0
    #USED TO CHECK IF THE PLAYER IS ON GROUND

  """
""""
  #update health
  def getHealth(self):
    if self.getHealth <= 0:
      print("Player Dead")
    else: 
      print("Life remaining: " + str(self.setHealth))

  #player movement left
  def playerMoveleft(self, x, y):
    event.key == pygame.K_LEFT:
    rate of change
    playerX_change = -0.3

  #player movement right
  def playerMoveright():
    event.key == pygame.K_RIGHT:
    #rate of change
    playerX_change = 0.3

  #player jump controls
  def jumpRange(self, x, y):
    event.type == pygame.KEYUP
    playerX_change = 4


  #basic laser
  def setWeapon(self):
    #screen.blit("player img with BASIC laser goes here" (x, y))

  #new laser
  def getWeapon(self):
    #screen.blit("player img with NEW laser goes here" (x, y))

  #laser movement
  def shootLaser(self):
    global laser_state
    laser_state = "fire"
    event.key == pygame.K_SPACE:
    fire_laser(playerX,laserY)
    #screen.blit("laser img goes here", (x+"#", y+"#"))

  #sound (SAL)
  #def sound():
  """