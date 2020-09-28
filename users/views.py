from users.models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from domecode.mixins import PageTitleMixin


def signup(request):
    return render(request, "users/register.html", {"title": "Register"})


class Leaderboard(PageTitleMixin, ListView):
    model = Profile
    template_name = "users/leaderboard.html"
    title = "Leaderboard"
    context_object_name = "profile"

    def get_queryset(self, *args, **kwargs):
        object_list = super(Leaderboard, self).get_queryset(*args, **kwargs)
        return object_list.order_by("-domes")[:100]


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your profile has been updated!")
            return redirect("users:profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "users/profile.html", context)


class AccountDetailView(PageTitleMixin, LoginRequiredMixin, DetailView):
    model = Profile
    title = "User Profile"
    template_name = "users/profilepage.html"
