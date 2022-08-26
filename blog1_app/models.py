from django.db import models
from datetime import datetime

# Create your models here.
#create db for core features on the blog

class Blog1(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

