from typing import List
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    RedirectView,
)
from django.db.models import Q
from . import compare
from domecode.mixins import PageTitleMixin

from django.conf import settings
from .models import Question, Answer
import requests
import json
import time


def coderhome(request):
    return render(request, "coder/coder_home.html", {"title": "Practice"})


class CoderListViewPy(PageTitleMixin, ListView):
    model = Question
    template_name = "coder/coder_list_python.html"
    context_object_name = "question"
    paginate_by = 15
    title = "Practice Python"

    def get_queryset(self, *args, **kwargs):
        object_list = super(CoderListViewPy, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get("q", None)
        if search:
            object_list = object_list.filter(
                Q(title__contains=search)
                | Q(content__contains=search)
                | Q(category__contains=search)
            )
            return object_list.filter(typeof="PYTHON")
        else:
            return object_list.filter(typeof="PYTHON")


class CoderListViewGen(PageTitleMixin, ListView):
    model = Question
    template_name = "coder/coder_list_common.html"
    context_object_name = "question"
    paginate_by = 15
    title = "Practice"

    def get_queryset(self, *args, **kwargs):
        object_list = super(CoderListViewGen, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get("q", None)
        if search:
            object_list = object_list.filter(
                Q(title__contains=search)
                | Q(content__contains=search)
                | Q(category__contains=search)
            )
            return object_list.filter(typeof="General")
        else:
            return object_list.filter(typeof="General")


class CoderListViewJava(PageTitleMixin, ListView):
    model = Question
    template_name = "coder/coder_list_java.html"
    context_object_name = "question"
    paginate_by = 15
    title = "Practice Java"

    def get_queryset(self, *args, **kwargs):
        object_list = super(CoderListViewJava, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get("q", None)
        if search:
            object_list = object_list.filter(
                Q(title__contains=search)
                | Q(content__contains=search)
                | Q(category__contains=search)
            )
            return object_list.filter(typeof="JAVA")
        else:
            return object_list.filter(typeof="JAVA")


class SubmissionListView(PageTitleMixin, LoginRequiredMixin, ListView):
    model = Answer
    template_name = "coder/submissions.html"
    context_object_name = "submission"
    paginate_by = 25
    title = "Your Submissions"

    def get_queryset(self, *args, **kwargs):
        object_list = Answer.objects.filter(user=self.request.user)
        return object_list


class CoderDetailView(PageTitleMixin, DetailView):
    model = Question
    template_name = "coder/coder_detail.html"
    context_object_name = "question"
    title = "Practice"


class CoderCreateView(PageTitleMixin, LoginRequiredMixin, CreateView):
    model = Answer
    fields = ["result", "language"]
    context_object_name = "answer"
    template_name = "coder/coder_form.html"
    title = "Submit"

    def get_success_url(self):
        question = self.object.question
        return reverse("coder:detail", kwargs={"slug": question.slug})

    def form_valid(self, form):
        form.instance.user = self.request.user
        question = Question.objects.get(slug=self.kwargs["qslug"])

        form.instance.question = question
        expected_output = question.solution.read().decode(
            "utf-8"
        )  # API won't compile this if you don't decode
        src_code = form.instance.result.read().decode("utf-8")

        # Judge API
        API_URL = "https://judge0.p.rapidapi.com/submissions/"
        querystring = {"base64_encoded": "false"}

        # Later change to wait = false
        headers_post = {
            "x-rapidapi-host": "judge0.p.rapidapi.com",
            "x-rapidapi-key": settings.JUDGE0_RAPID_API_KEY,
            "content-type": "application/json",
            "accept": "application/json",
        }

        LANGUAGE_CODES = {
            "PYTHON": 71,
            "JAVA": 62,
            "C++": 54,
            "RUST": 73,
            "GO": 60,
            "C": 50,
        }
        # Update above line whenever a new language is added

        data_post = {
            "source_code": src_code,
            "language_id": LANGUAGE_CODES[form.instance.language],
            "expected_output": expected_output,
        }
        data_post = json.dumps(data_post)
        response = requests.post(
            url=API_URL, data=data_post, headers=headers_post, params=querystring
        )
        token = json.loads(response.text)["token"]

        headers_get = {
            "x-rapidapi-host": "judge0.p.rapidapi.com",
            "x-rapidapi-key": settings.JUDGE0_RAPID_API_KEY,
        }
        status = "Processing"
        i = 0
        while status == "Processing" or status == "In Queue":
            response2 = requests.request(
                "GET", API_URL + token, headers=headers_get, params=querystring
            )
            status = json.loads(response2.text)["status"]["description"]
            time.sleep(0.1)
            i = i + 1
            if (
                i == 200
            ):  # Break if it takes more than 20 seconds (probably means api is down)
                status = "TLE"  # Setting the status = TLE
                break

        form.instance.status = status
        form.instance.response_from_judge = response2.text
        form.instance.iscorrect = form.instance.status == "Accepted"
        if (
            form.instance.iscorrect
            and Answer.objects.filter(question=question)
            .filter(iscorrect=True)
            .filter(user=form.instance.user)
            .count()
            == 0
        ):
            if form.instance.question.category == "EASY":
                form.instance.user.profile.domes += 10
            if form.instance.question.category == "MEDIUM":
                form.instance.user.profile.domes += 15
            if form.instance.question.category == "HARD":
                form.instance.user.profile.domes += 20
            if form.instance.question.category == "ADVANCED":
                form.instance.user.profile.domes += 30

        form.instance.user.profile.save()
        form.save()

        return super().form_valid(form)


"""
	def upload_file(request):
		if request.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				compare.compare(request.FILES['file'])
				return HttpResponseRedirect('/success/url/')
		else:
			form = UploadFileForm()
		return render(request, 'upload.html', {'form': form})

   #   form.instance.question.iscorrect = compare.compare((
  #      list(self.request.FILES.values())[0], question.solution), (list(self.request.FILES.values())[0], form.instance.result))
  #  form.instance.iscorrect = compare.compare(
   #     (list(self.request.FILES.values())[
        #     0].file.read(), question.solution),
        #   (list(self.request.FILES.values())[
        #   0].file.read(), form.instance.result)
        # )
"""
