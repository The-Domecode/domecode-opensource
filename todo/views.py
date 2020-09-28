from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo
from domecode.mixins import PageTitleMixin
from django.db.models import Q


class TodoListView(PageTitleMixin, LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "todo"
    paginate_by = 15
    title = "Your Tasks"

    def get_queryset(self, *args, **kwargs):
        object_list = super(TodoListView, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get("q", None)
        if search:
            object_list = object_list.filter(
                Q(title__icontains=search, user=self.request.user)
                | Q(content__icontains=search, user=self.request.user)
            ).order_by("created")
            return object_list
        else:
            object_list = Todo.objects.filter(user=self.request.user).order_by(
                "created"
            )
            return object_list


class TodoUpdateView(
    PageTitleMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = Todo
    success_url = reverse_lazy("todo:list")
    title = "Update Task"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Todo = self.get_object()
        if self.request.user == Todo.user:
            return True


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy("todo:list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def test_func(self):
        Todo = self.get_object()
        if self.request.user == Todo.user:
            return True


class TodoCreateView(PageTitleMixin, LoginRequiredMixin, CreateView):
    model = Todo
    fields = ["title", "content"]
    success_url = reverse_lazy("todo:list")
    title = "Create Task"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
