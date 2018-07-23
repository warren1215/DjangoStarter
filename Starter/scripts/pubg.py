from ..models import Season, PubgStat
from chicken_dinner.pubgapi import PUBG, PUBGCore
import json

region = "pc-na"
api = PUBG('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhYTdkY2Q1MC02NmUyLTAxMzYtYzlhZi03ZDVmNTRhMTMwOGYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTMxMjc3MjQ1LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRqYW5nbyJ9.7b3koP1ul3-1Zt24ytVZp2NI-Tuf5DJFmCBgO1r_6xg',
            region)
core = PUBGCore('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhYTdkY2Q1MC02NmUyLTAxMzYtYzlhZi03ZDVmNTRhMTMwOGYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTMxMjc3MjQ1LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRqYW5nbyJ9.7b3koP1ul3-1Zt24ytVZp2NI-Tuf5DJFmCBgO1r_6xg',
            region)


def getPlayerStats():
    player = api.players_from_names("Whale_Warren")[0]
    player_core = core.players("player_names", "Whale_Warren")
    id = player_core['data'][0]['id']
    name = player_core['data'][0]['attributes']['name']

    seasons = Season.objects.all()
    for season in seasons:
        stats = player.get_season(season)
        squad_fpp_stats = stats.game_mode_stats("squad", "fpp")
        if squad_fpp_stats['losses'] is not 0:
            kdr = round(squad_fpp_stats['kills'] / squad_fpp_stats['losses'], 2)
            PubgStat.objects.create(name=name, pubg_id=id, season=season, kdr=kdr)



def loadSeasons():
    Season.objects.all().delete()

    # Load all of the seasons into the database.

    seasons = api.seasons(region)
    for season in seasons:
        Season.objects.create(name=season.id, region=region)
