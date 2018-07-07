from django.urls import path
from Starter.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]