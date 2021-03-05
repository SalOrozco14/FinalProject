import pygame
"""
Animation creator

Animation function arguments 
FolderName : String
FileName : String
NumFiles : Int
FileType : String
Flip : Boolean  by default Flip is False and loads images as current file setup.
                If changed to True, it'll flip the images the opposite direction 
Size : Int will take in the current tile_size for the game

Example:
img/player[X].png

Animate("img","player",X,"png",False,tile_size)
"""


def Animate(FolderName, FileName, NumFiles, FileType, Flip, Size):
    img_list = []

    if Flip == False:
        for x in range(1, (NumFiles + 1)):
            img = pygame.image.load(FolderName + '/' + FileName + str(x) +
                                    '.' + FileType)
            img = pygame.transform.scale(img, (Size, Size))
            img_list.append(img)
            print("animation for loop: " + str(x))
    if Flip == True:
        for x in range(1, (NumFiles + 1)):
            img = pygame.image.load(FolderName + '/' + FileName + str(x) +
                                    '.' + FileType)
            img = pygame.transform.scale(img, (Size, Size))
            img = pygame.transform.flip(img, True, False)
            img_list.append(img)

    print('Animate Function Call')
    return img_list
