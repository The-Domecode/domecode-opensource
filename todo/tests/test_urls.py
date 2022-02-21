from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo.views import (
    TodoCreateView,
    TodoDeleteView,
    TodoListView,
    TodoDetailView,
    TodoUpdateView,
)


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolves(self):
        url = reverse("todo:list")
        self.assertEquals(resolve(url).func.view_class, TodoListView)

    def test_list_url_is_resolves_two(self):
        url = reverse("todo:detail", args=["3"])
        self.assertEquals(resolve(url).func.view_class, TodoDetailView)

    def test_list_url_is_resolves_two(self):
        url = reverse("todo:create")
        self.assertEquals(resolve(url).func.view_class, TodoCreateView)

    def test_list_url_is_resolves_two(self):
        url = reverse("todo:delete", args=["3"])
        self.assertEquals(resolve(url).func.view_class, TodoDeleteView)

    def test_list_url_is_resolves_two(self):
        url = reverse("todo:update", args=["3"])
        self.assertEquals(resolve(url).func.view_class, TodoUpdateView)
