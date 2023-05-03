import pygame
from constants import *
from Disk import Disk
from Tower import Tower
import time


def screen_output(tower_list):
    screen.blit(background, (0, 0))
    for i in range(len(tower_list)):
        Tower.add_tower_to_screen(tower_list[i])


def hanoi(num_discs, source, target, auxiliary, step_list):
    if num_discs == 1:
        step_list.append((source, target))
        return

    hanoi(num_discs - 1, source, auxiliary, target, step_list)
    step_list.append((source, target))
    hanoi(num_discs - 1, auxiliary, target, source, step_list)


def solve(tower_list, step_list):
    for i, (source, dest) in enumerate(step_list):
        disk = source.remove_disk()
        dest.add_disk(disk)
        screen_output(tower_list)


def main():
    pygame.init()
    pygame.display.set_caption('Hanoi Towers')

    disk_list = []

    # size, color
    d1 = Disk(1, (255, 0, 0))
    d2 = Disk(2, (0, 255, 255))
    d3 = Disk(3, (255, 255, 0))
    d4 = Disk(4, (51, 51, 255))
    d5 = Disk(5, (255, 0, 255))
    d6 = Disk(6, (102, 0, 51))
    d7 = Disk(7, (0, 102, 0))

    disk_list.append(d1)
    disk_list.append(d2)
    disk_list.append(d3)
    disk_list.append(d4)
    disk_list.append(d5)
    disk_list.append(d6)
    disk_list.append(d7)

    tower_list = []

    # list, x_pos
    t1 = Tower(disk_list, 1)
    t2 = Tower([], 2)
    t3 = Tower([], 3)

    tower_list.append(t1)
    tower_list.append(t2)
    tower_list.append(t3)

    for i in range(7-disk_quantity):
        del disk_list[-1]

    running = True
    step_list = []
    hanoi(disk_quantity, t1, t3, t2, step_list)
    solved = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        if not solved:
            solve(tower_list, step_list)
            solved = True

        pygame.display.flip()


if __name__ == "__main__":
    main()



