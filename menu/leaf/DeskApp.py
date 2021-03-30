from config.ConfigWriter import ConfigWriter
from input.InputButton import InputButton
from menu.Menu import Menu
import time

class DeskApp(Menu):

    OPTIONS = ["Stand", "Sit"]

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
        self.up_button = False
        self.down_button = False
        self.desk_control = self.repository['desk_control']

    def get_line_2_text(self, menu_config):
        return "TEST"

    def get_line_2_overlay(self, menu_config):
        return "_"

    def handle_input(self, input_button, menu_stack, menu_config):
        if input_button == InputButton.up:
            self.desk_control.go_up()
            time.sleep(9.25)
            self.desk_control.go_up(False)
        else:
            if input_button == InputButton.down:
                self.desk_control.go_bottom()

    def select_down(self):
        pass

    def select_up(self):
        pass

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
