from django.views.generic.base import TemplateView
from .models import Person, Steam, PubgStat
from .scripts.steam import gamespulling
from .scripts.pubg import getPlayerStats, loadSeasons


class PubgView(TemplateView):

    template_name = "pubg.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        stats = PubgStat.objects.all()
        context['pubg_stats'] = stats

        return context


# An example of using an API (steam).
class SteamView(TemplateView):

    template_name = "steam.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # My steam API key.
        key = '3206A3A552DA6FBE2D7FD6DCE523026B'

        # Steam id is for warren1215's profile: 76561198097834692 - warren, 76561198034593027 - d, 76561197992328350 - t
        steamID = str(76561198050935364)

        # Getting all of my steam games and time played for each.
        games = gamespulling(steamID, key)

        steam_user = Steam.objects.create(steam_id=steamID)
        steam_user.set_initial(games)
        steam_user.filter_games()

        context['steam_user'] = steam_user

        # loadSeasons()
        getPlayerStats()

        return context
