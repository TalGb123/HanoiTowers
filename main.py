import pygame

from constants import *
from Disk import Disk
from Tower import Tower


def screen_output(tower_list: list[Tower], count):
    screen.blit(background, (0, 0))
    for tower in tower_list:
        tower.add_tower_to_screen()
    font = pygame.font.SysFont("Aharoni", 20)
    text_min_steps = font.render(
        f"Minimum Steps: {(2 ** DISK_QUANTITY) - 1}", True, (0, 0, 0)
    )
    text_steps = font.render(f"Your Steps: {count+1}", True, (0, 0, 0))
    screen.blit(text_min_steps, (20, 20))
    screen.blit(text_steps, (WINDOW_WIDTH - 150, 20))


def hanoi(num_discs, source, target, auxiliary, step_list):
    if num_discs == 1:
        step_list.append((source, target))
        return

    hanoi(num_discs - 1, source, auxiliary, target, step_list)
    step_list.append((source, target))
    hanoi(num_discs - 1, auxiliary, target, source, step_list)


def solve(tower_list, step_list, count):
    source = tower_list[step_list[count][0] - 1]
    dest = tower_list[step_list[count][1] - 1]
    disk = source.remove_disk()
    dest.add_disk(disk)
    screen_output(tower_list, count)


def main():
    pygame.init()
    pygame.display.set_caption("Hanoi Towers")

    disk_list = [
        Disk(7, (0, 102, 0)),
        Disk(6, (102, 0, 51)),
        Disk(5, (255, 0, 255)),
        Disk(4, (51, 51, 255)),
        Disk(3, (255, 255, 0)),
        Disk(2, (0, 255, 255)),
        Disk(1, (255, 0, 0)),
    ]

    disk_list = disk_list[len(disk_list) - DISK_QUANTITY :]

    tower_list = [Tower(disk_list, 1), Tower([], 2), Tower([], 3)]

    running = True
    step_list = []
    count = 0
    hanoi(DISK_QUANTITY, 1, 3, 2, step_list)
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
            clock.tick(3)

            if count == len(step_list):
                solved = True

        pygame.display.flip()


if __name__ == "__main__":
    main()
