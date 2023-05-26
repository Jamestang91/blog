from django import forms
from django.forms import ModelForm
from .models import Blogpost


class ListingForm(ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'summary', 'description', 'imageUrl', 'imageCaption', 'category', 'author']


class BlogSearchForm(forms.Form):
    form = forms.CharField()
    q = ''

