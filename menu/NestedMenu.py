from input.InputButton import InputButton
from menu.Menu import Menu


class NestedMenu(Menu):

    def __init__(self, title, children):
        super().__init__(title)
        self.children = children
        self.selection = 0

    def handle_input(self, input_button):
        if input_button == InputButton.up:
            self.select_up()
            print(self.selection)
        elif input_button == InputButton.down:
            self.select_down()
            print(self.selection)

    def select_down(self):
        self.selection = (self.selection + 1) % len(self.children)

    def select_up(self):
        if self.selection > 0:
            self.selection = self.selection - 1
        else:
            self.selection = len(self.children) - 1

    def get_line_1(self):
        current_selection = self.children[self.selection]
        return current_selection.get_title()

    def confirm(self, menu_stack):
        menu_stack.append(self.children[self.selection])

    def back(self, menu_stack):
        if len(menu_stack) > 1:
            menu_stack.pop()
