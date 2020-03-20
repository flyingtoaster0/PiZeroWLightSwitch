from input.InputButton import InputButton
from menu.Menu import Menu


class NestedMenu(Menu):

    def __init__(self, title, child_ids):
        super().__init__(title)
        self.child_ids = child_ids
        self.selection = 0

    def handle_input(self, input_button, menu_stack, menu_config):
        if input_button == InputButton.up:
            self.select_up()
            print(self.selection)
        elif input_button == InputButton.down:
            self.select_down()
            print(self.selection)
        elif input_button == InputButton.enter:
            self.confirm(menu_stack, menu_config)
        elif input_button == InputButton.back:
            self.back(menu_stack)

    def select_down(self):
        self.selection = (self.selection + 1) % len(self.child_ids)

    def select_up(self):
        if self.selection > 0:
            self.selection = self.selection - 1
        else:
            self.selection = len(self.child_ids) - 1

    def get_line_1(self, menu_config):
        current_selection = self.child_ids[self.selection]
        selected_menu = menu_config[current_selection]
        return selected_menu.get_title()

    def confirm(self, menu_stack, menu_config):
        selected_id = self.child_ids[self.selection]
        next_menu = menu_config[selected_id]
        menu_stack.append(next_menu)

    def back(self, menu_stack):
        if len(menu_stack) > 1:
            menu_stack.pop()
