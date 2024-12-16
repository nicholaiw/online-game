import pygame

class Camera(pygame.sprite.Group):


    def __init__(self):
        super().__init__()

        self.displaySurface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.halfWidth = self.displaySurface.get_size()[0] // 2
        self.halfHeight = self.displaySurface.get_size()[1] // 2

        self.zoomScale = 4
        self.resizeableSurfaceSize = (1000, 1000)
        self.resizeableSurface = pygame.Surface(self.resizeableSurfaceSize, pygame.SRCALPHA)
        self.resizeableSurfaceRectangle = self.resizeableSurface.get_rect(center=(self.halfWidth, self.halfHeight))
        self.resizeableSurfaceSizeVector = pygame.math.Vector2(self.resizeableSurfaceSize)
        self.resizeableSurfaceOffset = pygame.math.Vector2()
        self.resizeableSurfaceOffset.x = self.resizeableSurfaceSize[0] // 2 - self.halfWidth
        self.resizeableSurfaceOffset.y = self.resizeableSurfaceSize[1] // 2 - self.halfHeight




    def draw(self, target):

        self.offset.x = target.rect.centerx - self.halfWidth
        self.offset.y = target.rect.centery - self.halfHeight

        self.resizeableSurface.fill('#aaaaaa')

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offsetPosition = sprite.rect.topleft - self.offset + self.resizeableSurfaceOffset
            self.resizeableSurface.blit(sprite.image, offsetPosition)

        resizedSurface = pygame.transform.scale(self.resizeableSurface, self.resizeableSurfaceSizeVector * self.zoomScale)
        resizedSurfaceRectangle = resizedSurface.get_rect(center=(self.halfWidth, self.halfHeight))
        self.displaySurface.blit(resizedSurface, resizedSurfaceRectangle)
