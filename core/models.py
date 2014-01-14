__author__ = 'pranavkv'
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=21844)

    def __unicode__(self):
        return self.title


class User(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user_name