from django.urls import path
from . import views

app_name ='tarot'

urlpatterns = [
    path('draw_card/', views.draw_card, name='raw_card'),
    path('explain_card/',views.explain_card,name='exlain_card')
]