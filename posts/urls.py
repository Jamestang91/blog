from django.urls import path

from posts import views
from posts.views import HomeView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CatListView
urlpatterns = [
    path('catlist/<category_id>/', views.category_posts, name='category_posts'),
    # path('catlist/<int:pk>/', CatDetailView.as_view(), name='detail_list'),
    path('catlist/', CatListView.as_view(), name='cat_list'),
    path('displayCategory', views.displayCategory, name='displayCategory'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('<slug:slug>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_new/', BlogCreateView.as_view(), name='blog_new'),
    path("<slug:slug>", BlogDetailView.as_view(), name='blog_detail'),
    path('', HomeView.as_view(), name='home'),
]