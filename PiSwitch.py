from display.BreadcrumbPrinter import BreadcrumbPrinter
from display.DisplayRenderer import DisplayRenderer
from display.MainLoop import MainLoop
from hue.HueClient import HueClient
from input.AppInput import AppInput
from menu.MenuConfig import MenuConfig
from menu.MenuManager import MenuManager
from nanoleaf.NanoleafClient import NanoleafClient
import yaml


class PiSwitch:
    def __init__(self, sub_renderer, sub_input, desk_control):
        self.sub_renderer = sub_renderer
        self.sub_input = sub_input
        self.desk_control = desk_control

    def begin(self):

        with open("config.yml", 'r') as ymlfile:
            config = yaml.load(ymlfile, Loader=yaml.BaseLoader)

        # TODO: Abstract out these two YAML loads into a class that checks a folder or something.
        # Presumably, you could have any number of these.
        multi_platform_config = []
        with open("multi_platform_config.yml", 'r') as ymlfile:
            multi_platform_config_yml = yaml.load(ymlfile, Loader=yaml.FullLoader)
            for key, value in multi_platform_config_yml.items():
                multi_platform_config.append(value)

        bedroom_config = []
        with open("bedroom_config.yml", 'r') as ymlfile:
            bedroom_config_yml = yaml.load(ymlfile, Loader=yaml.FullLoader)
            for key, value in bedroom_config_yml.items():
                bedroom_config.append(value)

        hue_username = config['hue']['username']
        nanoleaf_auth_token = config['nanoleaf']['auth_token']

        hue_url = 'http://' + config['hue']['ip']
        nanoleaf_url = 'http://' + config['nanoleaf']['ip'] + ':16021'

        # TODO: Init this async or something and fail properly. Have a failure "app" or something.
        hue_client = HueClient(hue_url, hue_username)
        nanoleaf_client = NanoleafClient(nanoleaf_url, nanoleaf_auth_token)

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
            'multi_platform_config': multi_platform_config,
            'bedroom_config': bedroom_config,
            'desk_control': self.desk_control,
            'hue_ip': config['hue']['ip'],
            'nanolead_ip': config['nanoleaf']['ip']
        }

        app_input = AppInput([self.sub_input])
        renderer = DisplayRenderer(self.sub_renderer)

        menu_config = MenuConfig().get_config(repository)
        root_menu = menu_config['menu1']
        menu_stack = [root_menu]

        breadcrumb_printer = BreadcrumbPrinter(menu_stack)
        menu_manager = MenuManager(menu_stack, menu_config, breadcrumb_printer)
        display = MainLoop(app_input, renderer, menu_manager, breadcrumb_printer)
        display.run()

    def init_repository(self):
        pass
