from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login',views.login_user,name='login_user'),
    path('accounts/register',views.register_user,name='register_user')   
]