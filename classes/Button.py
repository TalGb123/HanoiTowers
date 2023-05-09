import pygame


class Button:
    """
    A class used to represent an Button on the screen
    """
    # hovered = False

    def __init__(self, x_pos, y_pos, width, height):
        """
        Constructor

        :param x_pos: int
            Position of the top left corner of the button in X axis
        :param y_pos: int
            Position of the top left corner of the button in Y axis
        :param width: int
            Width of button in pixels
        :param height: int
            Height of button in pixels
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
    #     self.set_rect()
    #     self.draw()
    #
    # def draw(self):
    #     self.set_rend()
    #     screen.blit(self.rend, self.rect)
    #
    # def set_rend(self):
    #     self.rend = menu_font.render(self.text, True, self.get_color())
    #
    # def set_rect(self):
    #     self.set_rend()
    #     self.rect = self.rend.get_rect()
    #     self.rect.topleft = self.pos
    #
    # def get_color(self):
    #     if self.hovered:
    #         return (250, 50, 10)
    #     else:
    #         return (255, 255, 255)