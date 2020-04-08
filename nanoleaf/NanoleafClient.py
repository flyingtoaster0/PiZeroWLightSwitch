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


    def set_properties(self, nanoleaf_properties):
        state_url = self.base_url + '/state'
        effects_url = self.base_url + '/effects'

        on_off = nanoleaf_properties['on_state'] or True

        state_properties = {'on': {'value': on_off}}
        effect_properties = None

        if on_off is True:
            brightness = nanoleaf_properties['brightness']
            effect = nanoleaf_properties['effect']
            if brightness is not None:
                brightness_int = int((float(brightness) / 100) * 255)
                state_properties['brightness'] = {'brightness': self.wrap_value(brightness_int)}
            if effect is not None:
                effect_properties = {'select': effect}

        if effect_properties is not None:
            requests.put(effects_url, json.dumps(effect_properties))

        requests.put(state_url, json.dumps(state_properties))


    def wrap_value(self, value):
        return {'value': value}
