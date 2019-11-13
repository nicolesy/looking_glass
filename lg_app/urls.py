from . import views
from django.urls import path

app_name = "lg_app"
urlpatterns = [
    path("", views.index, name = "index"),
]