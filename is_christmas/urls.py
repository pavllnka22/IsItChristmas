from django.urls import path
from is_christmas import views, admin

urlpatterns = [
    path('', views.is_christmas, name='is_christmas'),

]
