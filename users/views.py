from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, EditProfileForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(CustomUser, user=user)
    return render(request, 'base.html', {'profile': profile, 'user': user})


@login_required
def edit_profile(request):
    if request.method == "POST":
        # request.user.username is the original username
        form = EditProfileForm(request.user.username, request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            age = form.cleaned_data["age"]
            # country = form.cleaned_data["country.name"]
            occupation = form.cleaned_data["occupation"]
            email = form.cleaned_data["email"]

            user = CustomUser.objects.get(id=request.user.id)
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.age = age
            # user.country = country
            user.occupation = occupation
            user.email = email

            user.save()

            return redirect("home")
    else:
        form = EditProfileForm(request.user.username)
    return render(request, "registration/edit_profile.html", {'form': form})
