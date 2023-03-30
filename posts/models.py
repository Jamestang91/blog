from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.urls import reverse

from commerce import settings


class Bannerpost(models.Model):
    objects = None
    bannerUrl = models.CharField(max_length=500)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    breakPage = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title


class Categories(models.Model):
    objects = None
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category_name}"


class Blogpost(models.Model):
    # fields of the model
    objects = None
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    description = RichTextUploadingField(blank=True, null=True)
    imageUrl = models.CharField(max_length=500)
    imageCaption = models.CharField(max_length=500)
    category = models.ForeignKey(Categories, on_delete=models.SET_DEFAULT, default="",
                                 blank=True, null=True, related_name="displayCategory")
    slug = models.SlugField(null=False, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
