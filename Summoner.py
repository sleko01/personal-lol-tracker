from riotwatcher import LolWatcher, ApiError
import config
import time


class Summoner:
    watcher = LolWatcher(config.APIFetcher.get_api_key())
    matches = watcher.match.matchlist_by_puuid('europe', config.APIFetcher.get_puuid())

    def __init__(self, name, region):
        self.info = None
        self.name = name
        self.region = region
        self.generate_info()
        self.stats = self.get_ranked_stats()
        config.APIFetcher.set_puuid(self.info['puuid'])  # enables finding matches for different summoners

    def get_name(self):
        return self.name

    def get_region(self):
        return self.region

    def get_ranked_stats(self):
        ranked_stats = Summoner.watcher.league.by_summoner(self.get_region(), self.info['id'])
        return ranked_stats

    def generate_info(self):
        self.info = Summoner.watcher.summoner.by_name(self.get_region(), self.get_name())

    def get_current_soloq_rank(self):
        return str(self.get_ranked_stats()[1]['tier'] + self.get_ranked_stats()[1]['rank'])

    def get_current_flex_rank(self):
        return str(self.get_ranked_stats()[0]['tier'] + self.get_ranked_stats()[0]['rank'])

    def get_current_soloq_lp(self):
        return self.get_ranked_stats()[1]['leaguePoints']

    def get_current_flex_lp(self):
        return self.get_ranked_stats()[0]['leaguePoints']

    def get_current_soloq_wins(self):
        return self.get_ranked_stats()[1]['wins']

    def get_current_soloq_losses(self):
        return self.get_ranked_stats()[1]['losses']

    def get_current_flex_wins(self):
        return self.get_ranked_stats()[0]['wins']

    def get_current_flex_losses(self):
        return self.get_ranked_stats()[0]['losses']

    @staticmethod
    def get_last_game():
        last_game = Summoner.matches[0]
        match_detail = Summoner.watcher.match.by_id('europe', last_game)
        return match_detail

    @staticmethod
    def get_last_game_duration():
        return Summoner.get_last_game()['info']['gameDuration'] / 60  # game duration in minutes

    @staticmethod
    def get_last_game_date():  # game date is defined by the date at the start of the game, not at the end
        epoch_time = Summoner.get_last_game()['info']['gameStartTimestamp']
        local_time_of_game_start = time.strftime('%Y-%m-%d', time.localtime(epoch_time / 1000))
        return local_time_of_game_start

    @staticmethod
    def get_last_game_gamemode():
        # this can be written as just return Summoner.get_last_game()['info']['gameMode']
        if Summoner.get_last_game()['info']['gameMode'] == "ARAM":
            return "ARAM"
        return "CLASSIC"  # API does not differentiate between different types of Summoner's Rift games
