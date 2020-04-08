class Menu:

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title, None

    def get_title_text(self):
        return self.title

    def get_line_1(self, menu_config, breadcrumb_printer):
        return self.get_line_1_text(menu_config, breadcrumb_printer), self.get_line_1_overlay(menu_config)

    def get_line_2(self, menu_config):
        return self.get_line_2_text(menu_config), self.get_line_2_overlay(menu_config)

    def get_line_3(self, menu_config):
        return self.get_line_3_text(menu_config), self.get_line_3_overlay(menu_config)

    def get_line_1_text(self, menu_config, breadcrumb_printer):
        return self.get_title_text()

    def get_line_2_text(self, menu_config):
        return None

    def get_line_3_text(self, menu_config):
        return None

    def get_line_1_overlay(self, menu_config):
        return None

    def get_line_2_overlay(self, menu_config):
        return None

    def get_line_3_overlay(self, menu_config):
        return None

    def get_renderable_text(self, menu_config, breadcrumb_printer):
        return [self.get_line_1(menu_config, breadcrumb_printer), self.get_line_2(menu_config), self.get_line_3(menu_config)]

    def handle_input(self, input_button, menu_stack, menu_config):
        pass

    def on_enter(self):
        pass
