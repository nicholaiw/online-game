from variables import *
from gameScene.scene import gameScene
from startScene.scene import *
from ui import *

network.startReceiving()
network.sendConnect()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    gameScene()
    drawText('hi', font, '#ffffff', 0, 0)

    pygame.display.flip()
    clock.tick(60)

network.sendDisconnect()
pygame.quit()
network.client.close()
