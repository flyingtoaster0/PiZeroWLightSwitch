import pygame

from input.InputButton import InputButton


class PyGameInput:

    input_map = {
        pygame.K_UP: InputButton.up,
        pygame.K_DOWN: InputButton.down,
        pygame.K_LEFT: InputButton.left,
        pygame.K_RIGHT: InputButton.right,
        pygame.K_RETURN: InputButton.enter,
        pygame.K_BACKSPACE: InputButton.back,
        pygame.K_ESCAPE: InputButton.quit,
    }

    def __init__(self):
        self.button_callback = None

    def begin_input(self):

        clock = pygame.time.Clock()
        done = False
        while not done:
            button = self.get_button()

            if button is not None:
                if button == InputButton.quit:
                    done = True  # Flag that we are done so we exit this loop

                if self.button_callback is not None:
                    self.button_callback(button)


            clock.tick(60)

        pygame.quit()


    def get_button(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:
                return InputButton.quit

            if event.type != pygame.KEYDOWN:
                return None

            key_input = event.key
            if key_input in PyGameInput.input_map:
                return PyGameInput.input_map[key_input]

        return None

    def set_callback(self, button_callback):
        self.button_callback = button_callback
