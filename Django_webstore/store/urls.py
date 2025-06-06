from django.urls import path , re_path
from . import views 
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
# imported for loading images which has been uploaded from admin pannel
from django.conf import settings
from django.conf.urls.static import static


app_name = "store"
urlpatterns = [
    path("" , views.index , name='index'), # --> in views.py
    path("products/" , views.products , name="products"),
    path("product/<int:id>/" , views.product , name="product"),
    path("signup/" , views.signupView , name="signup"),
    path("signin/", auth_views.LoginView.as_view(template_name="signin.html") , name="signin"), #views.signinView
    path("signout/" , views.signoutView , name="signout"),
    path("profile/" , views.profileView , name="profile"),
    path("elements/" , views.elements , name="elements"),
    path("password_reset/" , auth_views.PasswordResetView.as_view(template_name='password_reset.html' , html_email_template_name='password_reset_email.html') , name="password_reset"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html') , name="password_reset_confirm"), #auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html') , name="password_reset_complete"),# auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete'), name='password_reset_complete'),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),  # ✅ Ensure this is here
    path("cart/" , views.view_cart , name="view_cart"),
    path("add_to_cart/<int:id>/" , views.add_to_cart , name="add_to_cart"),
    path("info_completion/" , views.info_completion , name="info_completion")
    #path('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path("categories/", views.categories , name="categories"),
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT) 
