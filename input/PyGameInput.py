import pygame

from input.InputButton import InputButton


class PyGameInput:

    def __init__(self):
        self.input_map = {
            pygame.K_UP: InputButton.up,
            pygame.K_DOWN: InputButton.down,
            pygame.K_LEFT: InputButton.left,
            pygame.K_RIGHT: InputButton.right,
            pygame.K_RETURN: InputButton.enter,
            pygame.K_BACKSPACE: InputButton.back,
        }

    def get_button(self, event):
        if event.type != pygame.KEYDOWN:
            return None

        key_input = event.key
        if key_input in self.input_map:
            return self.input_map[key_input]

        return None
