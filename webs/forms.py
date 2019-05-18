from django import forms
from .models import TextBin, FileBin

class TextForm(forms.ModelForm):

    class Meta:
        model = TextBin
        fields = ('text',)

class FileForm(forms.ModelForm):
    
     class Meta:
        model = FileBin
        fields = ('name', 'file',)