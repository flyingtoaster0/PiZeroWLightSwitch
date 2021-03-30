import RPi.GPIO as GPIO

from output.OutputPin import OutputPin


class GPIOOutput:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        for pin in OutputPin:
            GPIO.setup(pin.value, GPIO.OUT)

    def on(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def off(self, pin):
        GPIO.output(pin, GPIO.LOW)
