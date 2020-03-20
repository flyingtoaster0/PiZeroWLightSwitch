from input.InputButton import InputButton
from menu.Menu import Menu


class TestLeaf(Menu):

    def __init__(self, title, menu_config, repository):
        super().__init__(title)
        self.repository = repository
        self.menu_config = menu_config

    def handle_input(self, input_button, menu_stack, menu_config):
        if input_button == InputButton.enter:
            print('WOO! We have an app!')
            self.repository['hue_client'].set_group_state('7', False)

