from riotwatcher import LolWatcher, ApiError
import config


class Champion:
    watcher = LolWatcher(config.APIFetcher.get_api_key())
    versions = watcher.data_dragon.versions_for_region('eune')
    champions_version = versions['n']['champion']
    current_champ_list = watcher.data_dragon.champions(champions_version)

    def __init__(self, name):
        self.name = name
        self.info = self.generate_info()

    def get_name(self):
        return self.name

    def generate_info(self):
        return Champion.current_champ_list['data'][self.get_name()]
