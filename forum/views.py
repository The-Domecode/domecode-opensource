from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from .models import Query, Answer, Comment
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from domecode.mixins import PageTitleMixin


def guidelines(request):
    return render(request, "forum/guidelines.html", {"title": "Forum Guidelines"})


class QueryListView(PageTitleMixin, generic.ListView):
    model = Query
    template_name = "forum/query_list.html"
    paginate_by = 15
    context_object_name = "query"
    ordering = ["-last_modified"]
    title = "Forum"

    def get_queryset(self, *args, **kwargs):
        object_list = super(QueryListView, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get("q", None)
        if search:
            object_list = object_list.filter(
                Q(title__contains=search)
                | Q(content__contains=search)
                | Q(category__contains=search)
            ).order_by("-last_modified")
            return object_list
        else:
            return object_list


class QueryDetailView(PageTitleMixin, generic.DetailView):
    model = Query
    template_name = "forum/query_detail.html"
    title = "Forum"


class QueryCreateView(PageTitleMixin, LoginRequiredMixin, generic.CreateView):
    model = Query
    template_name = "forum/query_form.html"
    fields = ["title", "content", "category"]
    title = "Ask"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QueryUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, PageTitleMixin, generic.UpdateView
):
    model = Query
    fields = ["title", "content", "category"]
    title = "Edit Query"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        query = self.get_object()
        if self.request.user == query.user:
            return True


class QueryDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, PageTitleMixin, generic.DeleteView
):
    model = Query
    success_url = reverse_lazy("forum:list")
    title = "Delete Query"

    def test_func(self):
        query = self.get_object()
        if self.request.user == query.user:
            return True


class AnswerCreateView(LoginRequiredMixin, PageTitleMixin, generic.CreateView):
    model = Answer
    template_name = "forum/answer_form.html"
    fields = ["content"]
    title = "Answer"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.query = Query.objects.get(slug=self.kwargs["qslug"])
        return super().form_valid(form)


class AnswerUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, PageTitleMixin, generic.UpdateView
):
    model = Answer
    template_name = "forum/answer_form.html"
    fields = ["content"]
    title = "Edit Answer"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.user:
            return True


class AnswerDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, PageTitleMixin, generic.DeleteView
):
    model = Answer
    success_url = reverse_lazy("forum:list")
    title = "Delete Answer"

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.user:
            return True


class AcceptAnswerView(
    LoginRequiredMixin, UserPassesTestMixin, PageTitleMixin, generic.UpdateView
):
    model = Answer
    fields = ["isaccepted"]
    template_name = "forum/answer_accept.html"
    title = "Accept Answer"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.query.user:
            return True


class AnswerDetailView(PageTitleMixin, generic.DetailView):
    model = Answer
    template_name = "forum/answer_detail.html"
    title = "Answer"


class CommentCreateView(LoginRequiredMixin, PageTitleMixin, generic.CreateView):
    model = Comment
    template_name = "forum/comment_form.html"
    fields = ["content"]
    title = "Comment"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.answer = Answer.objects.get(slug=self.kwargs["aslug"])
        return super().form_valid(form)


class CommentUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, PageTitleMixin, generic.UpdateView
):
    model = Comment
    template_name = "forum/comment_form.html"
    fields = ["content"]
    title = "Edit Comment"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True


class CommentDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, PageTitleMixin, generic.DeleteView
):
    model = Comment
    success_url = reverse_lazy("forum:list")
    title = "Delete Comment"

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True


class QueryLikeToggle(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        # query = get_object_or_404(Query, slug=self.kwargs["slug"])
        slug = self.kwargs.get("slug")
        print(slug)
        obj = get_object_or_404(Query, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


class QueryLikeAPIToggle(APIView):
    authentication_classes = [
        SessionAuthentication,
    ]
    permission_clases = [
        IsAuthenticated,
    ]

    def get(self, request, slug=None):
        obj = get_object_or_404(Query, slug=slug)
        updated = False
        liked = False
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)

            updated = True
        data = {"updated": updated, "liked": liked}
        return Response(data)


"""
class AnswerLikeToggle(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        print(slug)
        obj = get_object_or_404(Answer, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


class AnswerLikeAPIToggle(APIView):
    authentication_classes = [SessionAuthentication, ]
    permission_clases = [IsAuthenticated, ]

    def get(self, request, slug=None, format=None):
        obj = get_object_or_404(Answer, slug=slug)
        updated = False
        liked = False
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)

            updated = True
        data = {
            'updated': updated,
            'liked': liked
        }
        return Response(data)
"""
