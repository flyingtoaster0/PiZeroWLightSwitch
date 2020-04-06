import RPi.GPIO as GPIO

class GPIOInput:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

    def get_button(self):
        return None
