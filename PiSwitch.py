from display.BreadcrumbPrinter import BreadcrumbPrinter
from display.DisplayRenderer import DisplayRenderer
from display.MainLoop import MainLoop
from display.PCRenderer import PCRenderer
from hue.HueClient import HueClient
from input.AppInput import AppInput
from input.PyGameInput import PyGameInput
from menu.MenuConfig import MenuConfig
from menu.MenuManager import MenuManager
from nanoleaf.NanoleafClient import NanoleafClient
import yaml

with open("config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.BaseLoader)

hue_username = config['hue']['username']
nanoleaf_auth_token = config['nanoleaf']['auth_token']

hue_url = 'http://' + config['hue']['ip']
nanoleaf_url = 'http://' + config['nanoleaf']['ip'] + ':16021'


hue_client = HueClient(hue_url, hue_username)
nanoleaf_client = NanoleafClient(nanoleaf_url)

#hue_client.get_groups()

#hue_client.set_group_state('7', True)
#nanoleaf_client.set_state(nanoleaf_auth_token, True)

repository = {
    'hue_client': hue_client,
    'nanoleaf_client': nanoleaf_client
}


# TODO: Have different driver classes. The PC one just gets a PyGameInput, and the RaspPi one gets both inputs.
app_input = AppInput([PyGameInput()])

# TODO: Have different driver classes, etc.
renderer = DisplayRenderer(PCRenderer())

menu_config = MenuConfig().get_config(repository)
root_menu = menu_config['menu1']
menu_stack = [root_menu]

## todo menu config in the manager constructor
menu_manager = MenuManager(menu_stack, menu_config)
breadcrumb_printer = BreadcrumbPrinter()
display = MainLoop(app_input, renderer, menu_manager, breadcrumb_printer)
display.run()


