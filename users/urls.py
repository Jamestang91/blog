from django.urls import path
from .views import SignUpView, edit_profile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("edit_profile/", edit_profile, name="edit_profile"),
]
