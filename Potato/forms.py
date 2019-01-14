from django import forms
from django.forms import ModelForm
from .models import Post

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'writer', 'contents',]
        
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)