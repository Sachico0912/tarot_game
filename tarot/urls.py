from django.urls import path
from .views import cards

app_name = 'tarot'

urlpatterns = [
    path('cards/', cards,name='cards'),
]