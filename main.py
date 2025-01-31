from variables import *
from gameState.gameState import gameState
from startState.startState import *
from ui import *

network.startReceiving()
network.sendData("connect;none")

activeStates.append(startState)




run = True
while run:    
    screen.fill("#000000")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            run = False



    for scenes in range(len(activeStates)):
        activeStates[scenes]()


    pygame.display.flip()
    clock.tick(60)

network.sendData("disconnect;none")
pygame.quit()
network.client.close()