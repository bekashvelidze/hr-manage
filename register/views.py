from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='მომხმარებლები')
            user.groups.add(group)
            # messages.success(response, (f"{user} წარმატებით დარეგისტრირდა!"))
            return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})


@login_required
def profile(response):
    if response.method == "POST":
        u_form = UserUpdateForm(response.POST, instance=response.user)
        p_form = ProfileUpdateForm(response.POST, response.FILES, instance=response.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user')
        else:
            u_form = UserUpdateForm(instance=response.user)
            p_form = ProfileUpdateForm(instance=response.user.profile)

        context = {"u_form": u_form, "p_form": p_form}

        return render(response, 'support/user.html', context)