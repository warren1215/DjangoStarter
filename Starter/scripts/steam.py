# This script contains methods belonging to the Steam web API
# that can collect information based on an user's gaming library.

import requests
import json


def gamespulling(steamid, apikey):
    # Returns the JSON data from the Steam API based of one's
    # Steam ID number and returns a dictionary of
    # gameids and minutes played.

    steaminfo = {
        'key': apikey,
        'steamid': steamid,
        'format': 'JSON',
        'include_appinfo': '1'
    }
    apiurl = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
    req = requests.get(apiurl, params=steaminfo)
    data = json.loads(req.content)
    return data['response']['games']
