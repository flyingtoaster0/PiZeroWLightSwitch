import pygame
import os


class CommandLineRenderer:

    def __init__(self):
        pass

    def init_renderer(self):
        os.putenv('DISPLAY', ':0.0')
        pygame.init()

    def render(self, text_list):
        render_text = ''
        for tuple in text_list:
            for text in tuple:
                if text is not None:
                    render_text = render_text + text

        print(render_text, end='\r')
