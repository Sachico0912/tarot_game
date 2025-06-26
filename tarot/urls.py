from django.urls import path
from .views import draw_cards

app_name = 'tarot'

urlpatterns = [
    path('draw_cards/', draw_cards, name='draw_cards'),
]