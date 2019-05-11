from django.db import models

class Content(models.Model):
    dp = models.ImageField(upload_to='images/')
    short_des = models.TextField()
    bio = models.TextField(null=True)
    education = models.TextField(null=True)
    skill = models.TextField(null=True)
    interest = models.TextField(null=True)
    resume = models.FileField(upload_to='files/', null=True)


class Project(models.Model):
    title = models.TextField(blank=True)
    full_des = models.TextField(blank=True)
    tools = models.TextField(blank=True)
    references = models.TextField(blank=True)
    github_link = models.TextField(blank=True)
    category = models.TextField()
    ongoing = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    pic = models.ImageField(upload_to='images/', blank=True)
