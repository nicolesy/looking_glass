from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'users'
urlpatterns = [
    path('', views.login_register, name='login_register'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    # url(r'^password/$', views.change_password, name='change_password'),
    url('change_password', views.change_password, name='change_password'),
]