

class DisplayRenderer:

    def __init__(self, sub_renderer):
        self.sub_renderer = sub_renderer

    def init_renderer(self):
        self.sub_renderer.init_renderer()

    def render(self, text_list):
        if self.sub_renderer is None:
            return
        self.sub_renderer.render(text_list)

    def clear(self):
        self.sub_renderer.clear()
