from django.urls import path

from posts import views
from posts.views import HomeView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("displayCategory", views.displayCategory, name="displayCategory"),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('<slug:slug>/edit/', BlogUpdateView.as_view(), name='blog_edit'),  # new
    path('blog_new/', BlogCreateView.as_view(), name='blog_new'),  # new
    path("<slug:slug>", BlogDetailView.as_view(), name='blog_detail'),
    path('', HomeView.as_view(), name='home'),
]