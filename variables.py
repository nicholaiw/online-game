import pygame
from network import Network


pygame.init()
pygame.font.init()
screenWidth = 600
screenHeight = 400
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("online game")
clock = pygame.time.Clock()

HOST = 'localhost'
PORT = 5555

network = Network(HOST, PORT)

activeScenes = []