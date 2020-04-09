class CommandLineRenderer:

    def __init__(self):
        pass

    def init_renderer(self):
        pass

    def render(self, text_list):
        render_text = ''
        for tuple in text_list:
            for text in tuple:
                if text is not None:
                    render_text = render_text + text

        print(render_text, end='\r')
