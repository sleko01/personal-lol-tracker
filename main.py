# this program needs to gather information from Riot API and export them into a spreadsheet
# stuff that needs to be gathered: LP gain/loss, gamemode, win/loss, number of kills,
# deaths and assists, kda, cs, cs/min, champion I played, role I played, LP gain/loss
# this project will one day be written properly (if you are reading this, you have the time so do it!)
# information gathered: game duration, date of game,
# most of the code is still in "self-documenting" stage, but will one day be properly commented
from riotwatcher import LolWatcher, ApiError
import config
import pandas as pd  # this will be used to export data into excel spreadsheet
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
        if Summoner.get_last_game()['info']['gameMode'] == "ARAM":
            return "ARAM"
        return "CLASSIC"  # API does not differentiate between different types of Summoner's Rift games


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


def main():  # just a playground for testing functionality for now
    watcher = LolWatcher(config.APIFetcher.get_api_key())
    my_region = 'eun1'

    me = watcher.summoner.by_name(my_region, 'Darko Bundek')
    puuid = 'vRcJBT69hPYI4W5NnxWnDsKY-bI0e1Dih7gTAx5KHzGkZtIJXQ9wjxAWMTTTzrIkF-87544a9GCAvA'
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    print(my_ranked_stats)
    print(me)

    # Return the rank status for Darko Bundek
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    print(my_ranked_stats)

    my_matches = watcher.match.matchlist_by_puuid('europe', puuid)
    # fetch last match detail
    print(my_matches)

    last_match = my_matches[2]
    match_detail = watcher.match.by_id('europe', last_match)
    print(match_detail)
    # taking the current number of lp of account
    lp = my_ranked_stats[1]['leaguePoints']
    print("XD")
    print(lp)
    game_duration = match_detail['info']['gameDuration'] / 60  # game duration in minutes
    print(game_duration)
    gamemode = match_detail['info']['gameMode']
    print(gamemode)
    versions = watcher.data_dragon.versions_for_region('eune')
    champions_version = versions['n']['champion']
    current_champ_list = watcher.data_dragon.champions(champions_version)
    # print(current_champ_list)
    rakan = current_champ_list['data']['Rakan']
    print(rakan)
    ja = Summoner("Darko Bundek", "eun1")
    print(ja.stats)
    print(ja.get_current_soloq_rank())
    print(ja.get_current_soloq_lp())
    print(ja.get_current_soloq_wins())
    print(ja.get_current_soloq_losses())
    print(ja.get_last_game())
    print(ja.get_last_game_duration())
    print(ja.get_last_game_date())
    print(ja.get_last_game_gamemode())
    syndra = Champion("Syndra")
    syndra_name = syndra.get_name()
    print(syndra_name)
    print(syndra.info)

    return 0


main()
