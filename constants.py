import pygame


# window creation
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 1067
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pole = pygame.image.load("images/pole.png")
pole = pygame.transform.scale(pole, (32, 350))

# disk setting
DISK_QUANTITY = 3
DISK_WIDTH = 80
DISK_HEIGHT = 25

# restart button creation
RESTART_X_POS = 370
RESTART_Y_POS = 10
RESTART_WIDTH = 50
RESTART_HEIGHT = 50
restart_pic = pygame.image.load("images/restart_button.png")
restart_pic = pygame.transform.scale(restart_pic, (RESTART_WIDTH, RESTART_HEIGHT))

# arrow down+up button creation
ARROW_UP_X_POS = 430
ARROW_UP_Y_POS = 0
ARROW_DOWN_X_POS = 616
ARROW_DOWN_Y_POS = 0
ARROW_WIDTH = 100
ARROW_HEIGHT = 70
arrow_up_pic = pygame.image.load("images/arrow_up_button.png")
arrow_up_pic = pygame.transform.scale(arrow_up_pic, (ARROW_WIDTH, ARROW_HEIGHT))
arrow_down_pic = pygame.image.load("images/arrow_down_button.png")
arrow_down_pic = pygame.transform.scale(arrow_down_pic, (ARROW_WIDTH, ARROW_HEIGHT))

# disk monitor creation
MONITOR_X_POS = 470
MONITOR_Y_POS = 0
MONITOR_WIDTH = 156.25
MONITOR_HEIGHT = 70
MONITOR_NUM_X_POS = 549
MONITOR_NUM_Y_POS = 35
monitor_pic = pygame.image.load("images/disk_monitor.png")
monitor_pic = pygame.transform.scale(monitor_pic, (MONITOR_WIDTH, MONITOR_HEIGHT))

# blit spacers
HORIZONTAL_SPACE = 180
VERTICAL_SPACER = 455

# miscellaneous
start_rect = pygame.Rect(0, 0, WINDOW_WIDTH-100, 100)
start_rect.center = (WINDOW_WIDTH/2, 225)
clock = pygame.time.Clock()
FPS = 30
