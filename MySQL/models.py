from __future__ import unicode_literals

from django.db import models

# Create your models here.
class songxin(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=10)

