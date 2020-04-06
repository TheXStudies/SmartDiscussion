from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=128)
    text = models.TextField()


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
