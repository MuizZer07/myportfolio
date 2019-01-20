from django.db import models

class Content(models.Model):
    dp = models.ImageField(upload_to='images/')
    short_des = models.TextField()
    bio = models.TextField(null=True)
    resume = models.FileField(upload_to='files/', null=True)
