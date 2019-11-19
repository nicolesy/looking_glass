from . import views
from django.urls import path

app_name = "lg_app"
urlpatterns = [
    path("", views.index, name = "index"),
    path("get_presets/", views.get_presets, name = "get_presets"),
    path("upload_photo/", views.upload_photo, name = "upload_photo"),
    path("profile/", views.profile_page, name = "profile_page"),
    path("about/", views.about_page, name = "about_page"),
    path("select_presets/", views.select_presets, name = "select_presets"),
    path('add_fave/<int:pack_id>/', views.add_fave, name='add_fave'),
]