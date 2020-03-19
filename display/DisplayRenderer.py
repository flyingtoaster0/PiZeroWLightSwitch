

class DisplayRenderer:

    def __init__(self, sub_renderer):
        self.sub_renderer = sub_renderer

    def render(self, text_list):
        if self.sub_renderer is None:
            pass
        self.sub_renderer.render(text_list)
