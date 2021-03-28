from menu.NestedMenu import NestedMenu
from menu.leaf.BedroomApp import BedroomApp
from menu.leaf.DenApp import DenApp
from menu.leaf.HueRoomToggle import HueRoomToggle
from menu.leaf.HueIpApp import HueIpApp


class MenuConfig:

    def get_config(self, repository):
        return {
            'menu1': NestedMenu('Home', ['den_control', 'room_toggle', 'bedroom_control', 'settings']),
            'room_toggle': HueRoomToggle('Room Toggle', [], repository),
            'den_control': DenApp('Den Control', [], repository),
            'bedroom_control': BedroomApp('Bedroom Control', [], repository),
            'settings': NestedMenu('Settings', ['hue_ip_app']),
            'hue_ip_app': HueIpApp('Hue IP', [], repository)
        }
