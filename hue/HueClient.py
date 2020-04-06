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

    def set_group_hue(self, group_id, hue):
        url = self.set_group_state_url + '/' + group_id + '/action'
        request_body = json.dumps({'hue': hue})
        requests.put(url, request_body)

    def set_group_brightness(self, group_id, brightness):
        url = self.set_group_state_url + '/' + group_id + '/action'
        request_body = json.dumps({'bri': brightness})
        requests.put(url, request_body)
