from display.BreadcrumbPrinter import BreadcrumbPrinter
from display.DisplayRenderer import DisplayRenderer
from display.MainLoop import MainLoop
from display.PCRenderer import PCRenderer
from display.CommandLineRenderer import CommandLineRenderer
from hue.HueClient import HueClient
from input.AppInput import AppInput
from input.PyGameInput import PyGameInput
from menu.MenuConfig import MenuConfig
from menu.MenuManager import MenuManager
from nanoleaf.NanoleafClient import NanoleafClient
import yaml

with open("config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.BaseLoader)

multi_platform_config = []
with open("multi_platform_config.yml", 'r') as ymlfile:
    multi_platform_config_yml = yaml.load(ymlfile, Loader=yaml.FullLoader)
    for key, value in multi_platform_config_yml.items():
        multi_platform_config.append(value)

hue_username = config['hue']['username']
nanoleaf_auth_token = config['nanoleaf']['auth_token']

hue_url = 'http://' + config['hue']['ip']
nanoleaf_url = 'http://' + config['nanoleaf']['ip'] + ':16021'


hue_client = HueClient(hue_url, hue_username)
nanoleaf_client = NanoleafClient(nanoleaf_url, nanoleaf_auth_token)

#hue_client.get_groups()

#hue_client.set_group_state('7', True)
#nanoleaf_client.set_state(nanoleaf_auth_token, True)

# Section: Get hue groups.
hue_groups_response = hue_client.get_groups()
hue_groups = []
for key, value in hue_groups_response.items():
    if value['type'] == 'Room':
        value['id'] = key
        hue_groups.append(value)

repository = {
    'hue_client': hue_client,
    'hue_groups': hue_groups,
    'nanoleaf_client': nanoleaf_client,
    'multi_platform_config': multi_platform_config
}


# TODO: Have different driver classes. The PC one just gets a PyGameInput, and the RaspPi one gets both inputs.
app_input = AppInput([PyGameInput()])

# TODO: Have different driver classes, etc.
renderer = DisplayRenderer(PCRenderer())

menu_config = MenuConfig().get_config(repository)
root_menu = menu_config['menu1']
menu_stack = [root_menu]

## todo menu config in the manager constructor
breadcrumb_printer = BreadcrumbPrinter(menu_stack)
menu_manager = MenuManager(menu_stack, menu_config, breadcrumb_printer)
display = MainLoop(app_input, renderer, menu_manager, breadcrumb_printer)
display.run()


