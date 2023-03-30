from django.contrib import admin
from posts.models import Bannerpost, Blogpost, Categories


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Bannerpost)
admin.site.register(Blogpost, ArticleAdmin)
admin.site.register(Categories)
