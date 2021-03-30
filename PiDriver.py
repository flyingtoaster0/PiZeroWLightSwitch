from PiSwitch import PiSwitch
from desk.DeskControl import DeskControl
from display.PiRenderer import PiRenderer
from input.GPIOInput import GPIOInput

sub_renderer = PiRenderer()
sub_input = GPIOInput()
desk_control = DeskControl()

pi_switch = PiSwitch(sub_renderer, sub_input, desk_control)
pi_switch.begin()
