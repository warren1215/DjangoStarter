from django.urls import path
from .views import PubgView, SteamView

urlpatterns = [
    path('pubg', PubgView.as_view(), name='pubg'),
    path('steam', SteamView.as_view(), name='steam'),
]