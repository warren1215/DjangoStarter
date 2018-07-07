from django.views.generic.base import TemplateView
from .models import Person


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
