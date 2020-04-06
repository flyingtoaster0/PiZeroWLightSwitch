import requests
import json


class NanoleafClient:

    def __init__(self, base_url, auth_token):
        self.base_url = base_url + '/api/v1/' + auth_token

    # Note that auth_token here refers directly to a single device.
    def set_state(self, is_on):
        url = self.base_url + '/state'
        request_body = json.dumps({'on': {'value': is_on}})
        requests.put(url, request_body)

    def set_brightness(self, brightness):
        url = self.base_url + '/state'
        request_body = json.dumps({'brightness': {'value': brightness}})
        requests.put(url, request_body)

    def set_effect(self, effect_name):
        url = self.base_url + '/effects'
        request_body = json.dumps({'select': effect_name})
        requests.put(url, request_body)
