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
