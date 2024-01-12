from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"
    
# source: https://stackoverflow.com/questions/58794639/how-to-make-follower-following-system-with-django-model
class UserFollowing(models.Model):
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'following_user',)

    def __str__(self):
        return f"{self.user} follows {self.following_user}"

# Add likes / liked many to many rel with users
class Post(models.Model):
    content = models.CharField(max_length=280)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    posted_on = models.DateTimeField(default=timezone.now)

    def is_liked_by(self, user):
        return PostLikes.objects.filter(user=user, post=self).exists()

    def __str__(self):
        return f"{self.id}: posted by {self.posted_by} on {self.posted_on}"
    
class PostLikes(models.Model):
    user = models.ForeignKey(User, related_name="posts_liked", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post',)

    def __str__(self):
        return f"{self.user} likes {self.post}"