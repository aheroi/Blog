from dataclasses import field, fields
from pyexpat import model
from django import forms

from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
        widgets = {'title': forms.Textarea(attrs={'cols': 35}),
            'text': forms.Textarea(attrs={'cols': 80})}
