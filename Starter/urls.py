from django.urls import path
from .views import IndexView, SteamView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('steam', SteamView.as_view(), name='steam'),
]