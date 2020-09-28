from django.views.generic import ListView, DetailView, CreateView, UpdateView
from domecode.mixins import PageTitleMixin
from .models import Progress, Resource
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ResourcesHome(PageTitleMixin, ListView):
    model = Resource
    template_name = "resources/resources_home.html"
    title = "Tracks"
    context_object_name = "resource"


class ResourceDetailViewPy(PageTitleMixin, DetailView):
    model = Resource
    template_name = "resources/resources_detail_python.html"
    title = "Tracks - Python"

    def get_context_data(self, **kwargs):
        context = super(ResourceDetailViewPy, self).get_context_data(**kwargs)
        context["resources"] = Resource.objects.filter(language="PYTHON")
        return context

    def get_queryset(self, *args, **kwargs):
        object_list = Resource.objects.filter(language="PYTHON")
        return object_list


class ResourceDetailViewJava(PageTitleMixin, DetailView):
    model = Resource
    title = "Tracks - Java"
    template_name = "resources/resources_detail_java.html"

    def get_context_data(self, **kwargs):
        context = super(ResourceDetailViewJava,
                        self).get_context_data(**kwargs)
        context["resources"] = Resource.objects.filter(language="JAVA")
        return context

    def get_queryset(self, *args, **kwargs):
        object_list = Resource.objects.filter(language="JAVA")
        return object_list
