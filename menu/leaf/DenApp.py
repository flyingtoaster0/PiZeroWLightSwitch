from input.InputButton import InputButton
from menu.Menu import Menu


class DenApp(Menu):

    def __init__(self, title, menu_config, repository):
        super().__init__(title)
        self.repository = repository
        self.menu_config = menu_config
        self.hue_groups = repository['hue_groups']
        self.hue_client = repository['hue_client']
        self.nanoleaf_client = repository['nanoleaf_client']
        self.multi_platform_config = repository['multi_platform_config']
        self.selection_index = 0

    def get_line_2_text(self, menu_config):
        return self.multi_platform_config[self.selection_index]['name']

    def handle_input(self, input_button, menu_stack, menu_config):
        if input_button == InputButton.up:
            self.select_up()
        elif input_button == InputButton.down:
            self.select_down()
        elif input_button == InputButton.enter:

            room_config = self.multi_platform_config[self.selection_index]
            self.set_lights(room_config)

        elif input_button == InputButton.back:
            self.back(menu_stack)

    def select_down(self):
        self.selection_index = (self.selection_index + 1) % len(self.multi_platform_config)

    def select_up(self):
        if self.selection_index > 0:
            self.selection_index = self.selection_index - 1
        else:
            self.selection_index = len(self.multi_platform_config) - 1

    def back(self, menu_stack):
        if len(menu_stack) > 1:
            menu_stack.pop()

    def set_lights(self, room_config):
        self.hue_client.set_group_properties(room_config['hue_group_id'], room_config['hue_brightness'], room_config['hue_hue'], room_config['hue_saturation'])
        self.nanoleaf_client.set_effect(room_config['nanoleaf_effect'])
        self.nanoleaf_client.set_brightness(room_config['nanoleaf_brightness'])
