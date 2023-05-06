import pygame

# window creation
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 1067
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

# disk setting
DISK_QUANTITY = 4
DISK_WIDTH = 80
DISK_HEIGHT = 25

# restart button creation
RESTART_X_POS = 220
RESTART_Y_POS = 8
RESTART_WIDTH = 50
RESTART_HEIGHT = 50
restart_pic = pygame.image.load("images/restart_button.png")
restart_pic = pygame.transform.scale(restart_pic, (RESTART_WIDTH, RESTART_HEIGHT))

# arrow button creation
# arrow_vertices = [(200*(1/3), 100*(1/3)), (320*(1/3), 300*(1/3)), (80*(1/3), 300*(1/3))]  # [top, bottom right, bottom left]
# arrow_up_surface = pygame.Surface((400*1/3, 400*1/3))
# arrow_up_surface.set_colorkey((0, 0, 0))
# arrow_down_surface = pygame.transform.rotate(arrow_up_surface, 180)
# arrow_up = pygame.draw.polygon(arrow_up_surface, (2, 0, 0), arrow_vertices)
# arrow_down = pygame.draw.polygon(arrow_down_surface, (2, 0, 0), arrow_vertices)


# blit spacers
HORIZONTAL_SPACE = 180
VERTICAL_SPACER = 455

# miscellaneous
clock = pygame.time.Clock()
FPS = 30
