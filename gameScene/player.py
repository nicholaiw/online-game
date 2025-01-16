import pygame
import math
import pathlib

class Player(pygame.sprite.Sprite):
    def __init__(self, player_id, x=0, y=0, group=None):
        super().__init__(group) 


        self.id = player_id
        self.speed = 2
        self.image = self.loadSprite()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def loadSprite(self):
        currentFile = pathlib.Path(__file__)
        spritesDirectory = currentFile.parent.parent / "assets" / "sprites"
        spritesPath = spritesDirectory / "run.png"
        return pygame.image.load(str(spritesPath))



    def input(self):
        keys = pygame.key.get_pressed()
        directionX, directionY = 0, 0

        if keys[pygame.K_LEFT]:
            directionX -= 1
        if keys[pygame.K_RIGHT]:
            directionX += 1
        if keys[pygame.K_UP]:
            directionY -= 1
        if keys[pygame.K_DOWN]:
            directionY += 1

        if directionX != 0 or directionY != 0:
            length = math.sqrt(directionX**2 + directionY**2)
            directionX = directionX / length
            directionY = directionY / length
        self.movement(directionX * self.speed, directionY * self.speed)


    def movement(self, directionX, directionY):
        self.rect.x += directionX
        self.rect.y += directionY

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def updatePosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
