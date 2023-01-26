# this program needs to gather information from Riot API and export them into a spreadsheet
# stuff that needs to be gathered: LP gain/loss, gamemode, win/loss, number of kills,
# deaths and assists, kda, cs, cs/min, champion I played, role I played, LP gain/loss
# this project will one day be written properly (if you are reading this, you have the time so do it!)
# information gathered: game duration, date of game,
# most of the code is still in "self-documenting" stage, but will one day be properly commented
from riotwatcher import LolWatcher, ApiError
import config
import pandas as pd  # this will be used to export data into excel spreadsheet
from Champion import Champion
from Summoner import Summoner


def main():  # just a playground for testing functionality for now
    watcher = LolWatcher(config.APIFetcher.get_api_key())
    my_region = 'eun1'

    me = watcher.summoner.by_name(my_region, 'Darko Bundek')
    puuid = '2iAwqtDQdcWJwIrQG9xO4s4pbMvthVjGxUak_3AMeQxdVGd_YZs5qZtqw8VLX7L8W6IxCr5oWYc32A'
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
    # lp = my_ranked_stats[1]['leaguePoints']
    print("XD")
    # print(lp)
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
