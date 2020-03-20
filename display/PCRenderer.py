import pygame

# TODO: Pass title and message here
# TODO: idea: breadcrumbs!
# TODO: when rendering, maybe just pass this guy 4 lines of something. like a list of 4 strings.
class PCRenderer:

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.size = (1024, 128)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Test Window")

    def render(self, text_list):
        font = pygame.font.SysFont('Arial', 24, True, False)
        self.screen.fill(self.BLACK)

        text_y_position = 0
        for text in text_list:

            # "True" means anti-aliased renderable_text.
            renderable_text = font.render(text, True, self.WHITE)

            # Put the image of the renderable_text on the screen at 250x250
            self.screen.blit(renderable_text, [0, text_y_position * 32])
            text_y_position = text_y_position + 1

        # Draw
        pygame.display.flip()