from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # "" it means that after /polls we dont have any extra path so we set empty ""
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]