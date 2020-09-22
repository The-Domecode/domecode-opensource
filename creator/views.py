from django.urls import reverse_lazy
from django.views import generic
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from domecode.mixins import PageTitleMixin

"""
Product List View - Lists your products in the creator space (logged in, your
products)
Product Detail View - Lists a particular product for the public (public)
Product Create View - Create a product and manage it (logged in)
Product Update View - Update an existing product (sudo)
Product Delete View - Delete an existing product (sudo)

"""


class ProductListView(PageTitleMixin, LoginRequiredMixin, generic.ListView):
    model = Product
    title = "Your Products"
    template_name = "creator/product_list.html"
    context_object_name = "product"

    def get_queryset(self, *args, **kwargs):
        object_list = Product.objects.filter(user=self.request.user)
        return object_list


class ProductDetailView(PageTitleMixin, generic.DetailView):
    model = Product
    title = "Product Detail"
    template_name = "creator/product_detail.html"
    context_object_name = "product"


class ProductCreateView(PageTitleMixin, LoginRequiredMixin, generic.CreateView):
    model = Product
    title = "Create Product"
    template_name = "creator/product_form.html"
    fields = [
        "name",
        "description",
        "category",
        "github_Repo_Link",
        "producthunt",
        "youtube_videoid",
        "linkedin",
        "demo",
        "contributors",
        "isreleased",
        "documentation_Users_Link",
        "documentation_Devs_Link",
    ]
    context_object_name = "product"
    success_url = reverse_lazy("creator:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(
    PageTitleMixin, LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView
):
    model = Product
    title = "Update Product"
    template_name = "creator/product_form.html"
    fields = [
        "name",
        "description",
        "category",
        "github_Repo_Link",
        "producthunt",
        "youtube_videoid",
        "linkedin",
        "demo",
        "contributors",
        "isreleased",
        "documentation_Users_Link",
        "documentation_Devs_Link",
    ]

    context_object_name = "product"
    success_url = reverse_lazy("creator:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True


class ProductDeleteView(
    PageTitleMixin, LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView
):
    model = Product
    title = "Delete Product"
    template_name = "creator/product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("creator:list")

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
