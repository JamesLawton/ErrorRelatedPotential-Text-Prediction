import configparser

import pressagio.callback
import pressagio


# Define and create PresageCallback object
class DemoCallback(pressagio.callback.Callback):
    def __init__(self, buffer):
        super().__init__()
        self.buffer = buffer

    def past_stream(self):
        return self.buffer

    def future_stream(self):
        return ''


config_file = "example_profile.ini"
config = configparser.ConfigParser()
config.read(config_file)

callback = DemoCallback("Des is a Te")
prsgio = pressagio.Pressagio(callback, config)

predictions = prsgio.predict()