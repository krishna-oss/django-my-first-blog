from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('blog_details/<int:pk>/',views.blog_details,name='blog_details'),
    # path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name ='contact'),

    # path('accounts/login',views.login_user,name='login_user'),
    # path('accounts/register',views.register_user,name='register_user')
    
]