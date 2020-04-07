import RPi.GPIO as GPIO
from time import sleep

from input.InputButton import InputButton


class GPIOInput:

    def __init__(self):
        self.button_state_map = {
            InputButton.up: False,
            InputButton.down: False,
            InputButton.left: False,
            InputButton.right: False,
            InputButton.enter: False,
            InputButton.back: False,
        }

        self.gpio_button_map = {
            18: InputButton.up,
            22: InputButton.down,
            27: InputButton.left,
            23: InputButton.right,
            17: InputButton.enter,
            4: InputButton.back,
        }

        GPIO.setmode(GPIO.BCM)

        for input_pin, button in self.gpio_button_map.items():
            GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def get_button(self):

        for input_pin, button in self.gpio_button_map.items():

            button = self.gpio_button_map[input_pin]

            previous_state = self.button_state_map[button]

            current_button_state = GPIO.input(input_pin) == GPIO.HIGH

            self.button_state_map[button] = current_button_state

            state = self.button_state_map[button]

            if previous_state is False and state is True:
                print("gpio " + str(input_pin))
                return button

        return None

