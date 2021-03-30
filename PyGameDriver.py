from PiSwitch import PiSwitch
from desk.TestDeskControl import TestDeskControl
from display.PyGameRenderer import PyGameRenderer
from input.PyGameInput import PyGameInput

sub_renderer = PyGameRenderer()
sub_input = PyGameInput()
desk_control = TestDeskControl()

pi_switch = PiSwitch(sub_renderer, sub_input, desk_control)
pi_switch.begin()
