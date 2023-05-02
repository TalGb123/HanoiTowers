import pygame
from constants import *
from Disk import Disk


def draw_screen(disk_list, background):
    screen.blit(background, (0, 0))
    for i in range(len(disk_list)):
        Disk.draw_disk(disk_list[i])


def main():
    pygame.init()
    pygame.display.set_caption('Hanoi Towers')
    clock = pygame.time.Clock()

    background = pygame.image.load('images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    disk_list = []

    # size, image, color, x_pos, y_pos
    d1 = Disk(1, 'images/disk1.png', (255, 0, 0), 1, disk_quantity-6)
    d2 = Disk(2, 'images/disk2.png', (255, 0, 0), 1, disk_quantity-5)
    d3 = Disk(3, 'images/disk3.png', (255, 0, 0), 1, disk_quantity-4)
    d4 = Disk(4, 'images/disk4.png', (255, 0, 0), 1, disk_quantity-3)
    d5 = Disk(5, 'images/disk5.png', (255, 0, 0), 1, disk_quantity-2)
    d6 = Disk(6, 'images/disk6.png', (255, 0, 0), 1, disk_quantity-1)
    d7 = Disk(7, 'images/disk7.png', (255, 0, 0), 1, disk_quantity)

    disk_list.append(d1)
    disk_list.append(d2)
    disk_list.append(d3)
    disk_list.append(d4)
    disk_list.append(d5)
    disk_list.append(d6)
    disk_list.append(d7)

    for i in range(7-disk_quantity):
        del disk_list[-1]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        draw_screen(disk_list, background)
        pygame.display.flip()


if __name__ == "__main__":
    main()



# def hanoi(num_discs, source, target, auxiliary):
#     if num_discs == 1:
#         print(f"Move disc 1 from {source} to {target}")
#         return
#
#     hanoi(num_discs - 1, source, auxiliary, target)
#     print(f"Move disc {num_discs} from {source} to {target}")
#     hanoi(num_discs - 1, auxiliary, target, source)