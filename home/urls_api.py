
from django.urls import path
from .views_api import *

urlpatterns = [
    path('login/',loginView),
     path('register/',registerView)
]
