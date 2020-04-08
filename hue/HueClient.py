import requests
import json


class HueClient:

    def __init__(self, base_url, username):
        self.base_url = base_url
        self.username = username
        self.get_groups_url = self.base_url + '/api/' + self.username + '/groups'
        self.set_group_state_url = self.base_url + '/api/' + self.username + '/groups'

    def get_groups(self):
        response = requests.get(self.get_groups_url)
        groups_json = bytes.decode(response.content, 'ascii')
        return json.loads(groups_json)

    def set_group_state(self, group_id, is_on):
        url = self.set_group_state_url + '/' + group_id + '/action'
        request_body = json.dumps({'on': is_on})
        requests.put(url, request_body)

    def set_group_properties(self, hue_properties):
        group_id = hue_properties['group_id']
        url = self.set_group_state_url + '/' + group_id + '/action'

        on_off = hue_properties.get('on_state', False)

        properties = {'on': on_off}

        if on_off is True:
            hue = hue_properties.get('hue', None)
            saturation = hue_properties.get('saturation', None)
            brightness = hue_properties.get('brightness', None)
            if hue is not None:
                properties['hue'] = hue
            if brightness is not None:
                properties['bri'] = int((float(brightness) / 100) * 255)
            if saturation is not None:
                properties['sat'] = int((float(saturation) / 100) * 255)

        request_body = json.dumps(properties)
        requests.put(url, request_body)
