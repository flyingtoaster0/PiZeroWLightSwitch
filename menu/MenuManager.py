from input.InputButton import InputButton


class MenuManager:

    def __init__(self, menu_stack):
        self.menu_stack = menu_stack

    def get_renderable_text(self):
        return self.menu_stack[-1].get_renderable_text()

    def handle_input(self, input_button):
        if input_button is None:
            return

        current_menu = self.menu_stack[-1]

        if input_button == InputButton.enter:
            current_menu.confirm(self.menu_stack)
        elif input_button == InputButton.back:
            current_menu.back(self.menu_stack)

        current_menu.handle_input(input_button)


