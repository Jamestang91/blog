from django.forms import ModelForm
from .models import Blogpost


class ListingForm(ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'summary', 'description', 'imageUrl', 'imageCaption', 'category', 'author']
