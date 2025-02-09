from variables import *
from ui import *


def loadImage(image):
    currentFile = pathlib.Path(__file__)
    imageDirectory = currentFile.parent.parent / "assets" / "title"
    imageDirectory = imageDirectory / f"{image}.png"
    return pygame.image.load(str(imageDirectory))


mainImage = loadImage("main")
createImage = loadImage("create")
joinImage = loadImage("join")

widthMultiplier = 3.84
heightMultiplier = 3.75

mainImage = pygame.transform.scale(mainImage, (int(mainImage.get_width() * widthMultiplier), int(mainImage.get_height() * heightMultiplier)))
createImage = pygame.transform.scale(createImage, (int(createImage.get_width() * widthMultiplier), int(createImage.get_height() * heightMultiplier)))
joinImage = pygame.transform.scale(joinImage, (int(joinImage.get_width() * widthMultiplier), int(joinImage.get_height() * heightMultiplier)))

startImageRect = ((screen.get_width() - mainImage.get_width()) // 2, 
                  (screen.get_height() - mainImage.get_height()) // 2)


def startState():
    screen.blit(mainImage, startImageRect)
    createButton.actions()
    joinButton.actions()


    
def createState():
    screen.blit(createImage, startImageRect)
    createNameInput.actions()
    createNameInput.draw()
    createPlayButton.actions(createNameInput.text)



def joinState():
    screen.blit(joinImage, startImageRect)

    joinCodeInput.actions()
    joinNameInput.actions()

    joinCodeInput.draw()
    joinNameInput.draw()

    joinPlayButton.actions(f"{joinCodeInput.text};{joinNameInput.text}")

    

createButton = Button(64*widthMultiplier, 70*heightMultiplier, 80*widthMultiplier, 16*heightMultiplier, "changeState", createState)
joinButton = Button(64*widthMultiplier, 102*heightMultiplier, 80*widthMultiplier, 16*heightMultiplier, "changeState", joinState)

createNameInput = InputField(64*widthMultiplier, 72*heightMultiplier, 80*widthMultiplier, 16*heightMultiplier, '', "#97929a", 12)
createPlayButton = Button(87*widthMultiplier, 96 *heightMultiplier, 35*widthMultiplier, 16*heightMultiplier, "createGame")


joinCodeInput = InputField(64*widthMultiplier, 56*heightMultiplier, 80*widthMultiplier, 16*heightMultiplier, '', "#97929a", 6)
joinNameInput = InputField(64*widthMultiplier, 88*heightMultiplier, 80*widthMultiplier, 16*heightMultiplier, '', "#97929a", 12)
joinPlayButton = Button(87*widthMultiplier, 112 *heightMultiplier, 35*widthMultiplier, 16*heightMultiplier, "joinGame")
