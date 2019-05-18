from django.db import models

class Content(models.Model):
    dp = models.ImageField(upload_to='images/')
    short_des = models.TextField()
    bio = models.TextField(null=True)
    education = models.TextField(null=True)
    skill = models.TextField(null=True)
    interest = models.TextField(null=True)
    resume = models.FileField(upload_to='files/', null=True)

    def __str__(self):
        return "Profile Content"

class Tool(models.Model):
    tool = models.CharField(max_length=50)
    about = models.TextField(blank=True)
    my_expertise = models.TextField(blank=True)

    def __str__(self):
        return self.tool

class Project(models.Model):
    title = models.TextField(blank=True)
    full_des = models.TextField(blank=True)
    tools = models.ManyToManyField(Tool, blank=True)
    platform = models.TextField(blank=True)
    feature = models.TextField(blank=True)
    references = models.TextField(blank=True)
    github_link = models.URLField(blank=True)
    category = models.CharField(max_length=50)
    ongoing = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    description_lastupdated = models.DateField(auto_now=True, blank=True)
    pic = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title 

class TextBin(models.Model):
    text = models.TextField()
    imp = models.BooleanField(default=False)
    created = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.text 

class FileBin(models.Model):
    name = models.TextField(blank=True)
    file = models.FileField(upload_to='files/')
    imp = models.BooleanField(default=False)
    created = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.name