import pygame

from input.InputButton import InputButton


class MainLoop:

    def __init__(self, app_input, renderer, menu_manager, breadcrumb_printer):
        self.renderer = renderer
        self.app_input = app_input

        self.menu_manager = menu_manager
        self.breadcrumb_printer = breadcrumb_printer
        pass

    def run(self):
        self.renderer.init_renderer()

        clock = pygame.time.Clock()
        done = False

        while not done:
            button = self.app_input.get_button()

            if button == InputButton.quit:
                done = True  # Flag that we are done so we exit this loop

            self.menu_manager.handle_input(button)

            lines_to_render = self.menu_manager.get_renderable_text()

            self.renderer.render(lines_to_render)

            clock.tick(60)

        pygame.quit()
