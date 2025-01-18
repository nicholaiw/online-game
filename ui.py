from variables import *
import pathlib

def loadFont(font):
    currentFile = pathlib.Path(__file__)
    fontDirectory = currentFile.parent / "assets" / "fonts"
    fontPath = fontDirectory / f"{font}.ttf"
    return str(fontPath)


font = pygame.font.Font(loadFont('font'), 32)


def drawText(text, font, color, x , y):
    textSurface = font.render(text, True, color)
    screen.blit(textSurface, textSurface.get_rect(center=(x, y)))


