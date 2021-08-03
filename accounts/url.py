from django.urls import path
from django.contrib.auth import  views as auth_view
from . import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('change_password/',auth_view.PasswordChangeView.as_view(template_name='change_password.html'),
         name='password_change'),
    path('change_password/done/',auth_view.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),
         name='password_change_done'),


]