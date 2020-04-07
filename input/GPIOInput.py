import RPi.GPIO as GPIO

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
            4: InputButton.up,
            17: InputButton.down,
            18: InputButton.left,
            27: InputButton.right,
            22: InputButton.enter,
            23: InputButton.back,
        }

        GPIO.setmode(GPIO.BCM)

        for input_pin, button in self.gpio_button_map.items():
            GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def get_button(self):

        for input_pin, button in self.gpio_button_map.items():
            if self.check_map(input_pin) is True:
                return button

        return None

    def check_map(self, input_pin):
        button = self.gpio_button_map[input_pin]

        previous_state = self.button_state_map[button]

        current_button_state = GPIO.input(input_pin) == GPIO.HIGH

        self.button_state_map[button] = current_button_state

        state = self.button_state_map[button]

        return previous_state is False and state is True

