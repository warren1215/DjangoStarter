from django.views.generic.base import TemplateView
from .models import Person
from .scripts.steam import gamespulling


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Holds all data in the Person table.
        people = Person.objects.all()
        context['db_list'] = people

        # Holds the data from person table and a list of condensed dates.
        # This allows the template to iterate over both lists at the same time in a for loop.
        context['db_list_small_dates'] = zip(people, Person().small_dates())

        return context


# An example of using an API (steam).
class SteamView(TemplateView):

    template_name = "steam.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # My steam API key.
        key = '3206A3A552DA6FBE2D7FD6DCE523026B'

        # My steam id, for warren1215's profile.
        # 76561198097834692 - warren
        # 76561198034593027 - d
        # 76561197992328350 - t

        steamID = str(76561198097834692)

        # Getting all of my steam games and time played for each.
        games = gamespulling(steamID, key)
        context['game'] = games

        total_minutes = 0

        for game in games:
            total_minutes = total_minutes + int(game['playtime_forever'])

        context['total_minutes'] = total_minutes
        context['total_hours'] = int(total_minutes / 60)

        if total_minutes > 500000:
            help_status = "You need help"
        else:
            help_status = "rawr xd"

        context['need_help'] = help_status
        return context
