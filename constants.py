import pygame

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 1067
DISK_QUANTITY = 4
DISK_WIDTH = 80
HORIZONTAL_SPACE = 180
VERTICAL_SPACER = 455
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
SQUARE_HEIGHT = 25
clock = pygame.time.Clock()
FPS = 30
