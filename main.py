import pygame
from variables import *
from gameScene.scene import gameScene


network.startReceiving()
network.sendConnect()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    gameScene()


    pygame.display.flip()
    clock.tick(60)


network.sendDisconnect()
pygame.quit()
network.client.close()
