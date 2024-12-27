from django.urls import path

from . import views

urlpatterns = [
    # "" it means that after /polls we dont have any extra path so we set empty ""
    path("", views.index, name="index"), # in views.py file , run index function
    path("test" , view=views.test , name="test") # http://127.0.0.1:8000/polls/test
]