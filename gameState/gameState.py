from variables import *
from gameState.camera import Camera
from gameState.player import Player

spriteBatch = Camera()
localPlayer = Player()

def localPlayerInput():
    localPlayer.input()
    network.sendData(f'position;{localPlayer.rect.x},{localPlayer.rect.y}')

def drawPlayers():
    roomData = network.roomData
    if 'players' not in roomData:
        return

    cameraTarget = None

    for playerId, playerData in roomData['players'].items():
        if playerId not in [sprite.playerId for sprite in spriteBatch.sprites() if hasattr(sprite, 'playerId')]:
            newPlayer = Player()
            newPlayer.playerId = playerId
            spriteBatch.add(newPlayer)
        
        player = next((sprite for sprite in spriteBatch.sprites() if getattr(sprite, 'playerId', None) == playerId), None)
        if player:
            player.rect.x = playerData['positionX']
            player.rect.y = playerData['positionY']
            player.name = playerData['name']

        if playerId == network.clientID:
            cameraTarget = player

    for sprite in spriteBatch.sprites():
        if hasattr(sprite, 'playerId') and sprite.playerId not in roomData['players']:
            sprite.kill()

    return cameraTarget



def gameState():

    localPlayerInput()
    cameraTarget = drawPlayers()

    spriteBatch.update()
    spriteBatch.draw(cameraTarget)
