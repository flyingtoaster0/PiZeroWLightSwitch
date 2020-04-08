import pygame

class PyGameRenderer:

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.size = (512, 128)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Test Window")

    def init_renderer(self):
        pygame.init()

    def render(self, text_list):
        font_name = self.get_courier(pygame.font.get_fonts())
        font = pygame.font.SysFont(font_name, 24, True, False)
        self.screen.fill(self.BLACK)

        text_y_position = 0
        for tuple in text_list:
            for text in tuple:
                # "True" means anti-aliased renderable_text.
                renderable_text = font.render(text, True, self.WHITE)

                # Put the image of the renderable_text on the screen at 250x250
                self.screen.blit(renderable_text, [0, text_y_position * 32])

            text_y_position = text_y_position + 1
        # Draw
        pygame.display.flip()

    def get_courier(self, font_list):
        for font in font_list:
            if font.startswith('couriernew'):
                return font