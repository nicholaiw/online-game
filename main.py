from variables import *
from gameState.gameState import gameState
from startState.startState import *
from ui import *

network.startReceiving()
network.sendData("connect")
activeStates.append(startState)







run = True
while run:    
    screen.fill("#000000")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            run = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(network.roomData)


    if network.roomData:
        activeStates.clear()
        activeStates.append(gameState)

    for scenes in range(len(activeStates)):
        activeStates[scenes]()


    pygame.display.flip()
    clock.tick(60)

network.sendData("disconnect")
network.client.close()
pygame.quit()
