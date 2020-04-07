import RPi.GPIO as GPIO

from input.InputButton import InputButton


class GPIOInput:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.IN)

    def get_button(self):
        if GPIO.input(6):
            return InputButton.up
        return None
