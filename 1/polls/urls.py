from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # "" it means that after /polls we dont have any extra path so we set empty ""
    path("", views.index, name="index"), # in views.py file , run index function
    path("<int:question_id>/" , views.detail , name="detail"),
    path("<int:question_id>/results/" , views.results , name="results"),
    path("<int:question_id>/vote/" , views.vote , name="vote")
]
