from PiSwitch import PiSwitch
from display.PiRenderer import PiRenderer
from input.GPIOInput import GPIOInput

sub_renderer = PiRenderer()
sub_input = GPIOInput()

pi_switch = PiSwitch(sub_renderer, sub_input)
pi_switch.begin()
