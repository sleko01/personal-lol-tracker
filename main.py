# this program needs to gather information from Riot API in and export them into a spreadsheet
# stuff that needs to be gathered: date of game, length of game, gamemode, win/loss, number of kills,
# deaths and assists, kda, cs, cs/min, champion I played, role I played, LP gain/loss
# this project will one day be written properly (if you are reading this, you have the time so do it!)
# information gathered: LP gain/loss, game duration

from riotwatcher import LolWatcher, ApiError
import pandas as pd


class APIFetcher:
    def __init__(self, api_key, puuid):
        self.api_key = LolWatcher(api_key)
        self.puuid = puuid

    def get_api_key(self):
        return self.api_key

    def get_puuid(self):
        return self.puuid


class Summoner(APIFetcher):
    def __init__(self, name, region, api_key, puuid):
        super().__init__(api_key, puuid)
        self.name = name
        self.region = region

    def get_name(self):
        return self.name

    def get_region(self):
        return self.region


class Game(Summoner):
    def __init__(self, name, region, api_key, puuid):
        super().__init__(name, region, api_key, puuid)


def main():
    api_key = 'RGAPI-19293cde-ce4d-4008-9525-904634a37d0c'
    watcher = LolWatcher(api_key)
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
    return 0


main()
