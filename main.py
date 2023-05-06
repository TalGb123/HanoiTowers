import pygame
from constants import *
from classes.Disk import Disk
from classes.Tower import Tower
from classes.Button import Button
from buttons import *


def screen_output(tower_list: list[Tower], count):
    # background blit
    screen.blit(background, (0, 0))

    # disk draw
    for tower in tower_list:
        tower.add_tower_to_screen()

    # button blit
    screen.blit(restart_pic, (RESTART_X_POS, RESTART_Y_POS))
    # screen.blit(arrow_up_surface, (100, 100))

    # text blit
    font = pygame.font.SysFont("Aharoni", 20)
    text_min_steps = font.render(
        f"Minimum Steps: {(2 ** DISK_QUANTITY) - 1}", True, (0, 0, 0)
    )
    text_steps = font.render(f"Your Steps: {count+1}", True, (0, 0, 0))
    screen.blit(text_min_steps, (20, 20))
    screen.blit(text_steps, (WINDOW_WIDTH - 150, 20))


def initialize(disk_list):
    return [Tower(disk_list, 1), Tower([], 2), Tower([], 3)]


def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


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
    # window initialization
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

    # initialization of disk list (according to disk_quality) up to 7
    disk_list = disk_list[len(disk_list) - DISK_QUANTITY:]

    # tower list initialization
    tower_list = initialize(disk_list)

    # miscellaneous variables initialize
    running = True
    step_list = []
    count = 0
    solved = False

    # step list filling
    hanoi(DISK_QUANTITY, 1, 3, 2, step_list)

    # main loop
    while running:
        for event in pygame.event.get():
            # game quit
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # mouse click events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # restart button click check
                if mouse_in_button(restart_button, (mouse_pos[0], mouse_pos[1])):
                    tower_list = initialize(disk_list)
                    solved = False
                    count = 0

        # auto solver using step list
        if not solved:
            solve(tower_list, step_list, count)
            count += 1
            clock.tick(3)

            # locking the screen when solver finishes
            if count == len(step_list):
                solved = True

        pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    main()
