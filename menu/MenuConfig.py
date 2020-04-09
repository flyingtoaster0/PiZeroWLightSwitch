from menu.NestedMenu import NestedMenu
from menu.leaf.BedroomApp import BedroomApp
from menu.leaf.DenApp import DenApp
from menu.leaf.HueRoomToggle import HueRoomToggle


class MenuConfig:

    def get_config(self, repository):
        return {
            'menu1': NestedMenu('Home', ['den_control', 'room_toggle', 'bedroom_control']),
            'room_toggle': HueRoomToggle('Room Toggle', [], repository),
            'den_control': DenApp('Den Control', [], repository),
            'bedroom_control': BedroomApp('Bedroom Control', [], repository)
        }
