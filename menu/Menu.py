class Menu:

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def get_line_1(self, menu_config):
        return None

    def get_line_2(self, menu_config):
        return None

    def get_renderable_text(self, menu_config):
        return [self.title, self.get_line_1(menu_config), self.get_line_2(menu_config)]

    def handle_input(self, input_button, menu_stack, menu_config):
        pass
