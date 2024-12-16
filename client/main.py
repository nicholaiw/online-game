import pygame
from network import Network
from gameScene.player import Player
from gameScene.camera import Camera

width = 800
height = 600


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("online game")
clock = pygame.time.Clock()

HOST = 'localhost'
PORT = 5555

network = Network(HOST, PORT)

spriteBatch = Camera()
localPlayer = Player(network.playerId, group=spriteBatch)



network.startReceiving()
network.sendConnect()


def updatePlayer():
    localPlayer.input()
    network.sendPosition(localPlayer.getPosition())


def updateRemotePlayers():
    for playerId, data in network.players.items():
        if playerId not in [sprite.id for sprite in spriteBatch.sprites()]:
            spriteBatch.add(Player(playerId, data['x'], data['y'], group=spriteBatch))

        else:
            for sprite in spriteBatch.sprites():
                if sprite.id == playerId:
                    sprite.rect.topleft = (data['x'], data['y'])
                    break

                






run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    updatePlayer()
    updateRemotePlayers()




    spriteBatch.update()
    spriteBatch.draw(localPlayer)

    pygame.display.flip()
    clock.tick(60)


network.sendDisconnect()
pygame.quit()
network.client.close()
