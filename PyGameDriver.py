from PiSwitch import PiSwitch
from display.PyGameRenderer import PyGameRenderer
from input.PyGameInput import PyGameInput

sub_renderer = PyGameRenderer()
sub_input = PyGameInput()

pi_switch = PiSwitch(sub_renderer, sub_input)
pi_switch.begin()
