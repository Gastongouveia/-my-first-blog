from django import forms
from django.forms import fields
from .models import Post

class Postform(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text')
