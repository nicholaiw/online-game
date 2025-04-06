import pygame
from network import Network

pygame.init()
pygame.font.init()

screenMultiplier = 2.5
screenWidth = 400 * screenMultiplier
screenHeight = 250 * screenMultiplier
ratioMultiplier = 1.25 * screenMultiplier

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("online game")
clock = pygame.time.Clock() 

HOST = 'localhost'
PORT = 5555

network = Network(HOST, PORT)

activeStates = []