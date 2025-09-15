from django.urls import path
from SecretSanta import views, admin

urlpatterns = [
    path('', views.santa_page, name='santa_page'),
    path('pairs/', views.generate_pairs, name='pairs_page'),
    path('remove/<str:name>/', views.remove_participant, name='remove_participant'),
    path('clear/', views.clear_participants, name='clear_participants'),
]