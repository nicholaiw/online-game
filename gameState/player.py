import pygame
import math
import pathlib


class Player(pygame.sprite.Sprite):
    def __init__(self, group=None):
        super().__init__()

        self.playerId = None
        self.name = ""
        self.speed = 2
        self.image = self.loadSprite()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

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
