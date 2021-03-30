from config.ConfigWriter import ConfigWriter
from input.InputButton import InputButton
from menu.Menu import Menu
import time

class TestDeskApp(Menu):

    def __init__(self, title, menu_config, repository):
        super().__init__(title)
        self.repository = repository
        self.menu_config = menu_config
        self.hue_groups = repository['hue_groups']
        self.hue_client = repository['hue_client']
        self.nanoleaf_client = repository['nanoleaf_client']
        self.multi_platform_config = repository['multi_platform_config']
        self.selection_index = 0
        self.ip = ''
        self.overlay = '_'

    def get_line_2_text(self, menu_config):
        return "TEST"

    def get_line_2_overlay(self, menu_config):
        return "_"

    def handle_input(self, input_button, menu_stack, menu_config):
        if input_button == InputButton.enter:
            self.repository['desk_control'].go_up()

    def select_down(self):
        self.selection_index = (self.selection_index + 1) % len(self.OPTIONS)

    def select_up(self):
        if self.selection_index > 0:
            self.selection_index = self.selection_index - 1
        else:
            self.selection_index = len(self.OPTIONS) - 1

    def back(self, menu_stack):
        if len(menu_stack) > 1:
            menu_stack.pop()

    def set_lights(self, room_config):
        self.hue_client.set_group_properties(room_config['hue_properties'])
        self.nanoleaf_client.set_properties(room_config['nanoleaf_properties'])

    def confirm(self, menu_stack):
        self.ip = self.ip + self.OPTIONS[self.selection_index]
        ConfigWriter().write_hue_ip(self.ip)
        self.selection_index = 0
        self.ip = ''
        self.overlay = '_'
        menu_stack.pop()
