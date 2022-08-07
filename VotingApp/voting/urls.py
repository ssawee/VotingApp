from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', views.index),
    path('voting_model/<str:ct_model>/<str:slug>/', VotingDetailView.as_view(), name='voting_info'),
    path('character_model/<str:ct_model>/<str:slug>/', CharacterDetailView.as_view(), name='character_info'),
]
