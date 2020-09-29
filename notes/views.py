from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Notes
from django.db.models import Q
from domecode.mixins import PageTitleMixin


def home(request):
    return render(request, "notes/home.html", {"title": "Home"})


def about(request):
    return render(request, "notes/about.html", {"title": "About"})


def music(request):
    return render(request, "notes/musicpopup.html", {"title": "Music"})


def sponsor(request):
    return render(request, "notes/sponsor.html", {"title": "Sponsor"})


def privacy(request):
    return render(request, "notes/privacy.html", {"title": "Privacy Policy"})


def tos(request):
    return render(request, "notes/termsofservice.html",
                  {"title": "Terms of Service"})


class NotesListView(LoginRequiredMixin, PageTitleMixin, ListView):
    model = Notes
    context_object_name = "notes"
    title = "Your Notes"
    paginate_by = 15

    def get_queryset(self, *args, **kwargs):
        object_list = super(NotesListView, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get("q", None)

        if search:
            object_list = object_list.filter(
                Q(title__contains=search, user=self.request.user)
                | Q(content__contains=search, user=self.request.user)
                | Q(category__contains=search, user=self.request.user)
            ).order_by("-last_modified")
            return object_list
        else:
            object_list = Notes.objects.filter(
                user=self.request.user).order_by("-last_modified")
            return object_list


class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, PageTitleMixin,
                      UpdateView):
    model = Notes
    success_url = reverse_lazy("notes:list")
    title = "Update Note"
    fields = ["title", "content", "category"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.user:
            return True


class NotesDetailView(PageTitleMixin, LoginRequiredMixin, UserPassesTestMixin,
                      DetailView):
    model = Notes
    title = "Notes"

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.user:
            return True


class NotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, PageTitleMixin,
                      DeleteView):
    model = Notes
    success_url = reverse_lazy("notes:list")
    title = "Delete Note"

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.user:
            return True


class NotesCreateView(LoginRequiredMixin, PageTitleMixin, CreateView):
    model = Notes
    fields = ["title", "content", "category"]
    title = "Create Note"
    success_url = reverse_lazy("notes:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
