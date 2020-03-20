from menu.NestedMenu import NestedMenu
from menu.leaf.TestLeaf import TestLeaf


class MenuConfig:

    def get_config(self, repository):
        return {
            'menu1': NestedMenu('Menu 1', ['menu2', 'menu10', 'menu3', 'menu4'], repository),
            'menu2': NestedMenu('Menu 2', ['menu5', 'menu6', 'menu7'], repository),
            'menu3': NestedMenu('Menu 3', ['menu5', 'menu6', 'menu7'], repository),
            'menu4': NestedMenu('Menu 4', ['menu5', 'menu6', 'menu7'], repository),
            'menu5': NestedMenu('Menu 5', ['menu5', 'menu6', 'menu7'], repository),
            'menu6': NestedMenu('Menu 6', ['menu5', 'menu6', 'menu7'], repository),
            'menu7': NestedMenu('Menu 7', ['menu5', 'menu6', 'menu7'], repository),
            'menu8': NestedMenu('Menu 8', ['menu5', 'menu6', 'menu7'], repository),
            'menu9': NestedMenu('Menu 9', ['menu5', 'menu6', 'menu7'], repository),
            'menu10': TestLeaf('Test Leaf', ['menu5', 'menu6', 'menu7'], repository)
        }
