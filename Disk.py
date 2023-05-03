import pygame
from constants import *


class Disk:
    def __init__(self, size: int, color: tuple):
        self.size = size
        self.color = color

    def set_disk_pos(self, x_pos, y_pos):
        pass

    def draw_disk(self, x_pos, y_pos):
        square = pygame.Rect(0, 0, self.size*35,
                             SQUARE_HEIGHT)
        square.center = (HORIZONTAL_SPACE+(x_pos-1)*353, VERTICAL_SPACER-y_pos*25)
        pygame.draw.rect(screen, self.color, square)
