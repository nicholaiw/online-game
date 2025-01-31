from variables import *
from gameState.camera import Camera
from gameState.player import Player


spriteBatch = Camera()
localPlayer = Player(network.clientID, group=spriteBatch)


def updatePlayer():
    localPlayer.input()
    network.sendData(f'position,{localPlayer.rect.x},{localPlayer.rect.y}')


def updateRemotePlayers():
    for playerId, data in network.players.items():
        if playerId not in [sprite.id for sprite in spriteBatch.sprites()]:
            spriteBatch.add(Player(playerId, data['x'], data['y'], group=spriteBatch))

        else:
            for sprite in spriteBatch.sprites():
                if sprite.id == playerId:
                    sprite.rect.topleft = (data['x'], data['y'])
                    break




               

def gameState():
    cameraTarget = localPlayer
    updatePlayer()
    updateRemotePlayers()

    spriteBatch.update()
    spriteBatch.draw(cameraTarget) 
