import yaml

class ConfigWriter:

    def __init__(self):
        pass

    def write_hue_ip(self, ip):
        with open("config.yml", 'r') as ymlfile:
            config = yaml.load(ymlfile, Loader=yaml.BaseLoader)

        config["hue"]["ip"] = ip

        with open("config.yml", 'w') as ymlfile:
            written_config = yaml.dump(config, ymlfile)

    def write_nanoleaf_ip(self, ip):
        with open("config.yml", 'r') as ymlfile:
            config = yaml.load(ymlfile, Loader=yaml.BaseLoader)

        config["nanoleaf"]["ip"] = ip

        with open("config.yml", 'w') as ymlfile:
            written_config = yaml.dump(config, ymlfile)

