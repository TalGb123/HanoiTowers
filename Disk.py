import pygame.image
from constants import *


class Disk:
    def __init__(self, size, img_src, color, x_pos, y_pos):
        self.size = size
        self.img_src = img_src
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos

    def set_disk_pos(self, x_pos, y_pos):
        pass

    def draw_disk(self):
        img = pygame.image.load(self.img_src)
        img = pygame.transform.scale(img, (DISK_WIDTH+10*self.size, 50))
        screen.blit(img, (HORIZONTAL_SPACE+(self.x_pos-1)*350, VERTICAL_SPACER+self.y_pos*30))
