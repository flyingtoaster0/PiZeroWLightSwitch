class Menu:

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def get_line_1(self):
        return None

    def get_line_2(self):
        return None

    def get_renderable_text(self):
        return [self.title, self.get_line_1(), self.get_line_2()]

    def handle_input(self, input_button):
        pass
