from django.urls import path
from . import views 

app_name = "store"
urlpatterns = [
    path("" , views.index , name='index'),
    path("products/" , views.products , name="products"),
    #path("categories/", views.categories , name="categories"),
]


