from django.contrib import admin
from .models import Content, Project, Tool, FileBin, TextBin, top10s, Ratings, Tag

admin.site.register(Content)
admin.site.register(Project)
admin.site.register(Tool)
admin.site.register(TextBin)
admin.site.register(FileBin)
admin.site.register(top10s)
admin.site.register(Ratings)
admin.site.register(Tag)