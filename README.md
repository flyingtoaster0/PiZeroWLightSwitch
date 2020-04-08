# Raspberry Pi Light Switch

## Description

This is the software portion of an ongoing project to build a handheld device used to control **Philips Hue** and **Nanoleaf** lights through their publicly available APIs.

The project is designed to be run on [this 128 * 32 display from Adafruit](https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/overview).

Check out the project page on [Hackaday](https://hackaday.io/project/170825-raspberry-pi-huenanoleaf-light-swtich)

## Getting Started 

Run `python3 PiSwitch.py` to run the application.

### Dependencies

A few libraries are needed in order to run the project.

`pip3 install json PyYaml pygame==1.9.6`

#### Raspberry Pi Only
To run the project on a Raspberry Pi using GPIO and the 128 * 32 display, the additional libraries are needed.

`pip3 install RPi.GPIO adafruit-circuitpython-ssd1306`

Additionally, we need to install `python3-pil` which will us to render fonts on the display.

`sudo apt-get install python3-pil`

A full description of this display can be found [here](https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage).


### APIs

A file called `config.yml` is required to allow the Hue and Nanoleaf clients to operate.

`example_config.yml` has been included for reference:

```yaml
hue:
  ip: "192.168.x.x"
  username: "<hue_username>"
nanoleaf:
  ip: "192.168.y.y"
  auth_token: "<nanoleaf_auth_token>"
```

### Multiplatform Config
For easily creating configurations that affect both platforms, a file called `multi_platform_config.yml` is required.

This allows the creation of "scenes" or "settings" that involve both platforms. For example, setting an effect on a Nanoleaf panel, and dimming the Hue lights in a room.

`example_multi_platform_config.yml` has been included for reference:

```yaml
config_name:
  name: "Human Readable Title"
  hue_properties:
    on_state: true
    group_name: "Den"
    group_id: "7"
    brightness: 60
    hue: 8258
    saturation: 75
  nanoleaf_properties:
    effect: "Nanoleaf Effect Name"
    brightness: 65
    on_state: true
```

Acquiring the `hue_username` and `nanoleaf_auth_token` requires physical interaction with the Hue Bridge and Nanoleaf panels, respectively. Refer to their respective docs for details.

[Philips Hue API Docs](https://developers.meethue.com/develop/hue-api/) (Free account required)

[Nanoleaf API Docs](https://documenter.getpostman.com/view/1559645/RW1gEcCH?version=latest)

## Quick Documentation

### Main Loop

This project is primarily powered by a PyGame loop (`MainLoop`) that handles menus, input, and rendering.

### Menus
A simple menu system is included. The `Menu` class contains methods for handling displaying lines of text on the screen, as well as handling input.

`NestedMenu` is used for nested menu navigation. These can generally nest indefinitely.

Leaf `Menu`s can be thought of as "applications". Currently, only a few are implemented for controlling lights, but others can be made for configuring IP addresses, displaying system stats, etc.

### Display

The `DisplayRenderer` is there to abstract the render logic from the actual platform performing the rendering.

Currently, the following display implementations exist:

- `PyGameRenderer` (Launches a PyGame window scaled up from 128px * 32px)
- `PiRenderer` (For use with the 128 * 32 display)

#### Usage
```python
sub_renderer = PyGameRenderer()
renderer = DisplayRenderer(sub_renderer)
```

### Input

Specific input implementations have also been abstracted from `MainLoop`.

The different logical buttons are defined in `InputButton`.

```python
class InputButton(Enum):
    up = 1
    down = 2
    left = 3
    right = 4
    enter = 5
    back = 6
    quit = 7
```

`AppInput` abstracts the input logic. The following input implementations take care of converting actual input into the logical buttons defined above.

- `PyGameInput` (Uses keyboard input interpreted from PyGame events)
- `GPIOInput` (Reads GPIO pins on a Raspberry Pi)

#### Usage
Inputs are defined as a list to support using two at a time, if desired.
```python
input_list = [PyGameInput()]
app_input = AppInput(input_list)
```
