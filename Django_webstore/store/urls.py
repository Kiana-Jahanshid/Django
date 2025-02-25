from django.urls import path
from . import views 

app_name = "store"
urlpatterns = [
    path("" , views.index , name='index'), # --> in views.py
    path("products/" , views.products , name="products"),
    path("signup/" , views.signupView , name="signup"),
    path("signin/", views.signinView , name="signin"),
    path("signout/" , views.signoutView , name="signout"),
    path("profile/" , views.profileView , name="profile"),
    path("elements/" , views.elements , name="elements")
    #path("categories/", views.categories , name="categories"),
    #path("products/<int:product_id>/", views.product , name="product")
]


