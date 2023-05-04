import pygame
from constants import *
from Disk import Disk
from Tower import Tower


def screen_output(tower_list, count):
    screen.blit(background, (0, 0))
    for i in range(len(tower_list)):
        Tower.add_tower_to_screen(tower_list[i])
    font = pygame.font.SysFont("Aharoni", 20)
    text_min_steps = font.render(f"Minimum Steps: {(2 ** disk_quantity) - 1}", True, (0, 0, 0))
    text_steps = font.render(f"Your Steps: {count+1}", True, (0, 0, 0))
    screen.blit(text_min_steps, (20, 20))
    screen.blit(text_steps, (WINDOW_WIDTH-150, 20))


def hanoi(num_discs, source, target, auxiliary, step_list):
    if num_discs == 1:
        step_list.append((source, target))
        return

    hanoi(num_discs - 1, source, auxiliary, target, step_list)
    step_list.append((source, target))
    hanoi(num_discs - 1, auxiliary, target, source, step_list)


def solve(tower_list, step_list, count):
    source = tower_list[step_list[count][0]-1]
    dest = tower_list[step_list[count][1]-1]
    disk = source.remove_disk()
    dest.add_disk(disk)
    screen_output(tower_list, count)


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
    count = 0
    hanoi(disk_quantity, 1, 3, 2, step_list)
    solved = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        # screen_output(tower_list, count)
        if not solved:
            solve(tower_list, step_list, count)
            count += 1
            clock.tick(20)

            if count == len(step_list):
                solved = True

        pygame.display.flip()


if __name__ == "__main__":
    main()



