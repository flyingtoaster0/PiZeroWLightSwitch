from input.InputButton import InputButton
from menu.Menu import Menu


class TestLeaf(Menu):

    def __init__(self, title, menu_config, repository):
        super().__init__(title)
        self.repository = repository
        self.menu_config = menu_config
        self.hue_groups = repository['hue_groups']
        self.hue_client = repository['hue_client']
        self.selection_index = 0
        self.selection = None
        self.confirm_index = 0

    def handle_input(self, input_button, menu_stack, menu_config):
        if input_button == InputButton.up:
            self.select_up()
        elif input_button == InputButton.down:
            self.select_down()
        if input_button == InputButton.right:
            if self.selection is not None:
                self.confirm_index = (self.confirm_index + 1) % 2
                print(self.confirm_index)
        elif input_button == InputButton.left:
            if self.selection is not None:
                self.confirm_index = (self.confirm_index - 1) % 2
                print(self.confirm_index)
        elif input_button == InputButton.enter:
            if self.selection is None:
                self.selection = self.hue_groups[self.selection_index]
            else:
                on_off = self.confirm_index == 0
                self.hue_client.set_group_state(self.selection['id'], on_off)
        elif input_button == InputButton.back:
            if self.selection is None:
                self.back(menu_stack)
            else:
                self.selection = None
                self.confirm_index = 0

    def get_line_1_text(self, menu_config):
        return self.hue_groups[self.selection_index]['name']

    def get_line_2_text(self, menu_config):
        if self.selection is not None:
            return 'ON OFF'

    def get_line_2_overlay(self, menu_config):
        if self.selection is not None:
            if self.confirm_index == 0:
                return '__'
            else:
                return '   ___'

    def get_renderable_text(self, menu_config):
        return [self.get_line_1(menu_config), self.get_line_2(menu_config)]

    def select_down(self):
        if self.selection is None:
            self.selection_index = (self.selection_index + 1) % len(self.hue_groups)

    def select_up(self):
        if self.selection is None:
            if self.selection_index > 0:
                self.selection_index = self.selection_index - 1
            else:
                self.selection_index = len(self.hue_groups) - 1

    def back(self, menu_stack):
        if len(menu_stack) > 1:
            menu_stack.pop()
