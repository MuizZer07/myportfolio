from django.db import models

class Content(models.Model):
    dp = models.ImageField(upload_to='images/')
    short_des = models.CharField(max_length=700)