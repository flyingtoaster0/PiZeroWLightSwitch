import requests
import json


class NanoleafClient:

    def __init__(self, base_url):
        self.base_url = base_url + ':16021/api/v1/'

    # Note that auth_token here refers directly to a single device.
    def set_state(self, auth_token, is_on):
        url = self.base_url + auth_token + '/state'
        request_body = json.dumps({'on': {'value': is_on}})
        requests.put(url, request_body)
