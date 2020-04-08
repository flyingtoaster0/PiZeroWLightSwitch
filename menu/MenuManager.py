from input.InputButton import InputButton


class MenuManager:

# todo menu config constructor. need id in order to get it. may need to pass into config dict
    def __init__(self, menu_stack, menu_config, breadcrumb_printer):
        self.menu_stack = menu_stack
        self.menu_config = menu_config
        self.breadcrumb_printer = breadcrumb_printer

    def get_renderable_text(self):
        return self.menu_stack[-1].get_renderable_text(self.menu_config, self.breadcrumb_printer)

    def handle_input(self, input_button):
        if input_button is None:
            return

        current_menu = self.menu_stack[-1]
        current_menu.handle_input(input_button, self.menu_stack, self.menu_config)


