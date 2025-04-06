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



mainImage = pygame.transform.scale(mainImage, (int(mainImage.get_width() * ratioMultiplier), int(mainImage.get_height() * ratioMultiplier)))
createImage = pygame.transform.scale(createImage, (int(createImage.get_width() * ratioMultiplier), int(createImage.get_height() * ratioMultiplier)))
joinImage = pygame.transform.scale(joinImage, (int(joinImage.get_width() * ratioMultiplier), int(joinImage.get_height() * ratioMultiplier)))

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

    

createButton = Button(120*ratioMultiplier, 90*ratioMultiplier, 80*ratioMultiplier, 16*ratioMultiplier, "changeState", createState)
joinButton = Button(120*ratioMultiplier, 120*ratioMultiplier, 80*ratioMultiplier, 16*ratioMultiplier, "changeState", joinState)

createNameInput = InputField(120*ratioMultiplier, 93*ratioMultiplier, 80*ratioMultiplier, 16*ratioMultiplier, '', "#97929a", 12)
createPlayButton = Button(143*ratioMultiplier, 117 *ratioMultiplier, 35*ratioMultiplier, 16*ratioMultiplier, "createGame")


joinCodeInput = InputField(120*ratioMultiplier, 109*ratioMultiplier, 80*ratioMultiplier, 16*ratioMultiplier, '', "#97929a", 4)
joinNameInput = InputField(120*ratioMultiplier, 77*ratioMultiplier, 80*ratioMultiplier, 16*ratioMultiplier, '', "#97929a", 10)
joinPlayButton = Button(143*ratioMultiplier, 133 *ratioMultiplier, 35*ratioMultiplier, 16*ratioMultiplier, "joinGame")
