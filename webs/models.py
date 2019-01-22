from django.db import models

class Content(models.Model):
    dp = models.ImageField(upload_to='images/')
    short_des = models.TextField()
    bio = models.TextField(null=True)
    education = models.TextField(null=True)
    skill = models.TextField(null=True)
    interest = models.TextField(null=True)
    resume = models.FileField(upload_to='files/', null=True)
