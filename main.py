import pygame
from constants import *
from classes.Disk import Disk
from classes.Tower import Tower
from classes.Button import Button
from buttons import *
import random


# screen output in the pygame window
def screen_output(tower_list: list[Tower], count):
    # background blit
    screen.fill((233, 244, 255))
    plate = pygame.Rect(0, 468, WINDOW_WIDTH, 50)
    pygame.draw.rect(screen, (158, 153, 152), plate)
    for i in range(3):
        screen.blit(pole, (HORIZONTAL_SPACE+338+(i-1)*353, 118))

    # disk draw
    for tower in tower_list:
        tower.add_tower_to_screen()

    # button blit
    screen.blit(restart_pic, (RESTART_X_POS, RESTART_Y_POS))
    screen.blit(arrow_up_pic, (ARROW_UP_X_POS, ARROW_UP_Y_POS))
    screen.blit(arrow_down_pic, (ARROW_DOWN_X_POS, ARROW_DOWN_Y_POS))
    screen.blit(monitor_pic, (MONITOR_X_POS, MONITOR_Y_POS))

    # text font creation
    font_text = pygame.font.SysFont("Aharoni", 25)
    font_num = pygame.font.SysFont("Aharoni", 30)
    font_monitor_and_start = pygame.font.SysFont("Aharoni", 50)

    # font render with text
    text_min_steps1 = font_text.render(
        f"Minimum Steps:", True, (0, 0, 0)
    )
    text_min_steps2 = font_num.render(
        f"{(2 ** disk_quantity) - 1}", True, (0, 0, 0)
    )
    text_steps1 = font_text.render(
        f"Your Steps:", True, (0, 0, 0)
    )
    text_steps2 = font_num.render(
        f"{count + 1}", True, (0, 0, 0)
    )
    disk_monitor = font_monitor_and_start.render(
        f"{disk_quantity}", True, (0, 0, 0)
    )
    monitor_rect = disk_monitor.get_rect(center=(MONITOR_NUM_X_POS, MONITOR_NUM_Y_POS))
    not_start = font_monitor_and_start.render(
        "Press Anywhere but buttons to start", True, (0, 0, 0)
    )

    # text blit
    screen.blit(text_min_steps1, (20, 20))
    screen.blit(text_min_steps2, (210, 17))
    screen.blit(text_steps1, (WINDOW_WIDTH - 200, 20))
    screen.blit(text_steps2, (WINDOW_WIDTH - 60, 17))
    screen.blit(disk_monitor, monitor_rect)
    if not start:  # if solver hasn't started, it will show a message in the middle of the screen
        pygame.draw.rect(screen, (230, 204, 204), start_rect)
        screen.blit(not_start, (100, 200))


# restarts the game, sends all disks to the first tower to replay the solver
def initialize(disk_list):
    return [Tower(disk_list, 1), Tower([], 2), Tower([], 3)]


# returns the chosen disk quantity list and restarts the game
def new_disk_list():
    # initialization of disk list (according to disk_quality) up to 10 (or whatever we set it in the increase button)
    chosen_disk_list = []
    for i in reversed(range(1, disk_quantity+1)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        chosen_disk_list.append(Disk(i, (r, g, b)))
    return initialize(chosen_disk_list)


# checks if the mouse click is on the chosen button
def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


# the regular recursion towers of hanoi solver that save moves in step_list
def hanoi(num_discs, source, target, auxiliary, step_list):
    if num_discs == 1:
        step_list.append((source, target))
        return

    hanoi(num_discs - 1, source, auxiliary, target, step_list)
    step_list.append((source, target))
    hanoi(num_discs - 1, auxiliary, target, source, step_list)


# gets the step list from Hanoi function and automatically plays the game using the game loop (does each move)
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

    # miscellaneous variables for initialization initialize
    running = True
    step_list = []
    count = 0
    solved = False
    global disk_quantity
    disk_quantity = 3
    global start
    start = False

    # step list filling
    hanoi(disk_quantity, 1, 3, 2, step_list)

    # tower list initialization
    tower_list = new_disk_list()

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
                    tower_list = new_disk_list()
                    solved = False
                    count = 0
                    start = False

                # disk quantity add by 1 on arrow up button
                elif mouse_in_button(arrow_up, (mouse_pos[0], mouse_pos[1])):
                    if disk_quantity < 20:
                        disk_quantity += 1
                        step_list = []
                        hanoi(disk_quantity, 1, 3, 2, step_list)
                        tower_list = new_disk_list()
                        solved = False
                        count = 0
                        start = False

                # disk quantity substract by 1 on arrow down button
                elif mouse_in_button(arrow_down, (mouse_pos[0], mouse_pos[1])):
                    if disk_quantity > 1:
                        disk_quantity -= 1
                        step_list = []
                        hanoi(disk_quantity, 1, 3, 2, step_list)
                        tower_list = new_disk_list()
                        solved = False
                        count = 0
                        start = False

                if all([not mouse_in_button(restart_button, (mouse_pos[0], mouse_pos[1])),
                        not mouse_in_button(arrow_up, (mouse_pos[0], mouse_pos[1])),
                        not mouse_in_button(arrow_down, (mouse_pos[0], mouse_pos[1]))
                        ]):
                    start = True

        # starts only if the player clicked on the screen
        if start:
            # auto solver using step list
            if not solved:
                solve(tower_list, step_list, count)
                count += 1
                clock.tick(3)

                # locking the screen when solver finishes
                if count == len(step_list):
                    solved = True

        # outputs screen with a message while solver is not activated
        else:
            screen_output(tower_list, 0)

        pygame.display.flip()


if __name__ == "__main__":
    main()
