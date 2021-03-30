import time

class TestDeskControl:
    def __init__(self):
        pass

    def go_up(self, on=True):
        if on:
            print("Fake desk going up.")
        else:
            print("Fake desk stopping.")

    def go_down(self, on=True):
        if on:
            print("Fake desk going down")
        else:
            print("Fake desk stopping.")

    def go_bottom(self):
        print("Fake desk lowering fully.")
