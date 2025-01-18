from variables import *
from gameScene.scene import gameScene
from startScene.scene import startScene
from ui import *

network.startReceiving()
network.sendConnect()

activeScenes.append(gameScene)
activeScenes.append(startScene)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for scenes in range(len(activeScenes)):
        activeScenes[scenes]()

    pygame.display.flip()
    clock.tick(60)

network.sendDisconnect()
pygame.quit()
network.client.close()