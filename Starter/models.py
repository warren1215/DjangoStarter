from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def small_dates(self):
        people = Person.objects.all()
        dates = []
        for person in people:
            dates.append(person.pub_date.strftime("%Y-%m-%d"))
        return dates


class Steam(models.Model):
    steam_id = models.CharField(max_length=50)
    total_games = models.IntegerField(default=0)
    total_minutes = models.IntegerField(default=0)
    total_hours = models.IntegerField(default=0)
    total_years = models.CharField(max_length=5, null=True)
    help_status = models.CharField(max_length=50, null=True)
    all_games = models.CharField(max_length=100000, null=True)
    filtered_games = models.CharField(max_length=100000, null=True)

    def __str__(self):
        return self.steam_id

    def filter_games(self):
        filtered_games = []
        for game in self.all_games:
            if game['playtime_forever'] > 0:
                filtered_games.append({'name': game['name'], 'minutes_played': game['playtime_forever']})
        self.filtered_games = filtered_games

    def set_initial(self, games):
        total_minutes = 0
        total_games = 0

        for game in games:
            total_games = total_games + 1
            total_minutes = total_minutes + int(game['playtime_forever'])

        self.all_games = games
        self.total_games = total_games
        self.total_minutes = total_minutes
        self.total_hours = int(total_minutes / 60)
        self.total_years = str(round(self.total_hours / 8760, 2))

        if total_minutes > 500000:
            self.help_status = "You need help"
        else:
            self.help_status = "rawr xd"
