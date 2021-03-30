import time

from output.GPIOOutput import GPIOOutput
from output.OutputPin import OutputPin


class DeskControl:
    def __init__(self):
        self.gpio_output = GPIOOutput()

    def go_up(self):
        print("Going up!")
        self.gpio_output.on(OutputPin.desk_up.value)
        time.sleep(2)
        self.gpio_output.off(OutputPin.desk_up.value)
        print("Done going up.")
