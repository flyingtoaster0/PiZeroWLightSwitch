import pygame


class MainLoop:

    # TODO: Pass in a repo that can access the data.
    # TODO: Pass in a class that understands how to perform actions.
    def __init__(self, app_input, renderer, menu_manager, breadcrumb_printer):
        self.renderer = renderer
        self.app_input = app_input

        self.menu_manager = menu_manager
        self.breadcrumb_printer = breadcrumb_printer
        pass

    def run(self):
        pygame.init()

        clock = pygame.time.Clock()
        done = False

        while not done:
            for event in pygame.event.get():  # User did something

                button = self.app_input.get_button(event)

                self.menu_manager.handle_input(button)
                # if button == InputButton.left:
                #     print("ayy")

                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

## TODO: also add GPIO but through another class so that it's not imported directly here.
## todo: use whichever renderer is needed.

            breadcrumb_str = self.breadcrumb_printer.get_breadcrumb_str(self.menu_manager.menu_stack)
            lines_to_render = [breadcrumb_str] + self.menu_manager.get_renderable_text()

            self.renderer.render(lines_to_render)

            clock.tick(60)

        pygame.quit()
