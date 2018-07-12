import requests
import json
from pubg_python import PUBG, Shard


def getPlayerStats(playerid):
    # data['data']['attributes']['gameModeStats']['duo-fpp']['kills'] (Original PUBG API call)


    api = PUBG('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhYTdkY2Q1MC02NmUyLTAxMzYtYzlhZi03ZDVmNTRhMTMwOGYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTMxMjc3MjQ1LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRqYW5nbyJ9.7b3koP1ul3-1Zt24ytVZp2NI-Tuf5DJFmCBgO1r_6xg',
               Shard.PC_NA)

    players = api.players().filter(player_names=['Whale_Warren'])

    player_id = players[0]

    one_match = api.matches().get(player_id.matches[0].id)

    roster = one_match.rosters

    for player in roster:
        print(player.participants[0].name)
        if player.participants[0].name == "Whale_Warren":
            match_stats = player.participants[0]

    print(match_stats.damage_dealt)
