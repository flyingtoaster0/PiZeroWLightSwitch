from menu.NestedMenu import NestedMenu


class MenuConfig:

    def __init__(self):
        self.config = NestedMenu('Test Menu', [
            NestedMenu('Other menu', [
                NestedMenu("Third menu", [
                    NestedMenu("4th menu - Don't go here. No more children.", []),
                    NestedMenu("5th menu - Don't go here. No more children.", [])
                ])
            ]),
            NestedMenu('Other other menu', ['test', 'test'])
        ])
