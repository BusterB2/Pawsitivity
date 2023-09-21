from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
