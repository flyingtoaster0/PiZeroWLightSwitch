import time

from output.GPIOOutput import GPIOOutput
from output.OutputPin import OutputPin


class DeskControl:
    def __init__(self):
        self.gpio_output = GPIOOutput()

    def go_up(self, on=True):
        if on:
            self.gpio_output.on(OutputPin.desk_up.value)
        else:
            self.gpio_output.off(OutputPin.desk_up.value)

    def go_down(self, on=True):
        if on:
            self.gpio_output.on(OutputPin.desk_down.value)
        else:
            self.gpio_output.off(OutputPin.desk_down.value)

    def go_bottom(self):
        self.gpio_output.on(OutputPin.desk_down.value)
        self.gpio_output.on(OutputPin.desk_up.value)
        time.sleep(1)
        self.gpio_output.off(OutputPin.desk_up.value)
        self.gpio_output.off(OutputPin.desk_down.value)
