import pygame


class CommandLineRenderer:

    def __init__(self):
        pass

    def init_renderer(self):
        pygame.init()

    def render(self, text_list):
        render_text = ''
        for tuple in text_list:
            for text in tuple:
                render_text = render_text + text

        print(render_text, end='\r')
