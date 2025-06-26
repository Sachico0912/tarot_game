from django.urls import path
from .views import draw_card

app_name ='tarot'

urlpatterns = [
    path('draw_card/', draw_card, name='raw_card'),
]