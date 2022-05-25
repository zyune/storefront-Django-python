from django.urls import path
from . import views
# This is where we mapping url to views so when we input a url in a browser we know where to go 
urlpatterns = [
    path('hello/', views.say_hello),
]