from variables import *
from ui import *


nameInput = Input(screenWidth/2, screenHeight/2, 140, 32, '', 12 )


def loadImage(image):
    currentFile = pathlib.Path(__file__)
    imageDirectory = currentFile.parent.parent / "assets" / "title"
    imageDirectory = imageDirectory / f"{image}.png"
    return pygame.image.load(str(imageDirectory))

mainImage = loadImage("main")
mainImage = pygame.transform.scale(mainImage, (mainImage.get_width() * 3.84, mainImage.get_height() * 3.75))

#createImage = loadImage("create")
#joinImage = loadImage("join")




def startScene():

    

    nameInput.draw(screen)
    screen.blit(mainImage, 
                ((screen.get_width() - mainImage.get_width()) // 2, 
                 (screen.get_height() - mainImage.get_height()) // 2))