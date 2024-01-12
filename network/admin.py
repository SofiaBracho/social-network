from django.contrib import admin
from .models import User, UserFollowing, Post, PostLikes


# Register your models here.
admin.site.register(User)
admin.site.register(UserFollowing)
admin.site.register(Post)
admin.site.register(PostLikes)