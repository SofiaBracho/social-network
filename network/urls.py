
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following, name="following"),
    path("post", views.post, name="post"),
    path("post_edit/", views.post_edit, name="post_edit"),
    path("follow/", views.follow, name="follow"),
    path("like/", views.like, name="like"),
    path("<int:user_id>/profile/", views.profile, name="profile"),
]
