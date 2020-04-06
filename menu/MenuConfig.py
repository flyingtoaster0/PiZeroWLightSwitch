from menu.NestedMenu import NestedMenu
from menu.leaf.DenApp import DenApp
from menu.leaf.HueRoomToggle import HueRoomToggle


class MenuConfig:

    def get_config(self, repository):
        return {
            'menu1': NestedMenu('Menu 1', ['den_control', 'room_toggle', 'menu3', 'menu4']),
            'menu2': NestedMenu('Menu 2', ['menu5', 'menu6', 'menu7']),
            'menu3': NestedMenu('Menu 3', ['menu5', 'menu6', 'menu7']),
            'menu4': NestedMenu('Menu 4', ['menu5', 'menu6', 'menu7']),
            'menu5': NestedMenu('Menu 5', ['menu5', 'menu6', 'menu7']),
            'menu6': NestedMenu('Menu 6', ['menu5', 'menu6', 'menu7']),
            'menu7': NestedMenu('Menu 7', ['menu5', 'menu6', 'menu7']),
            'menu8': NestedMenu('Menu 8', ['menu5', 'menu6', 'menu7']),
            'menu9': NestedMenu('Menu 9', ['menu5', 'menu6', 'menu7']),
            'room_toggle': HueRoomToggle('Room Toggle', [], repository),
            'den_control': DenApp('Den Control', [], repository)
        }
