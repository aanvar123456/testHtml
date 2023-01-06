from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='das'),
    path('login', views.user_login, name='dasad')
]