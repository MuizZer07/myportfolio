from django.contrib import admin
from .models import Content, Project, Tool, FileBin, TextBin

admin.site.register(Content)
admin.site.register(Project)
admin.site.register(Tool)
admin.site.register(TextBin)
admin.site.register(FileBin)