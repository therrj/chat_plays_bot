import yaml

from constants import *
import utils

def _load_config():
    with open("config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
        return config

class Config():
    def __init__(self):
        yaml_config = _load_config()
        self.log_level = yaml_config[LOG_LEVEL]
        self.token = yaml_config[TWITCH_ACCESS_TOKEN]
        self.client_id = yaml_config[TWITCH_CLIENT_ID]
        self.nick = yaml_config[TWITCH_USERNAME]
        self.channel = yaml_config[TWITCH_CHANNEL]

        self.key_press_duration = int(yaml_config[KEY_PRESS_DURATION])
        self.key_press_scale_factor = int(yaml_config[KEY_PRESS_SCALE_FACTOR])
        self.key_press_duration_min = int(yaml_config[KEY_PRESS_DURATION_MIN])
        self.key_press_duration_max = int(yaml_config[KEY_PRESS_DURATION_MAX])

        # The config syntax should be easier for user inputs, but for matching
        # it's easier to flip the dictionary, so we'll do that now.
        self.key_inputs = utils.invert_dictionary(yaml_config[KEY_INPUTS])

    def __repr__(self):
        return (f"Log Level: {self.log_level}\n"
                f"Token: {self.token}\n"
                f"Client ID: {self.client_id}\n"
                f"Nick: {self.nick}\n"
                f"Channel: {self.channel}\n"
                f"Key Press Duration: {self.key_press_duration}\n"
                f"Key Press Scale Factor: {self.key_press_scale_factor}\n"
                f"Key Press Duration Min: {self.key_press_duration_min}\n"
                f"Key Press Duration Max: {self.key_press_duration_max}\n"
                f"Key Inputs: {self.key_inputs}")