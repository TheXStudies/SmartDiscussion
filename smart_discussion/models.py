from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=64)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

