from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=20)


class Position(models.Model):
	name = models.CharField(max_length=20)
