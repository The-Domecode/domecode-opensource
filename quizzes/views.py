from coder.models import Question
from django.shortcuts import render
from .models import Ques, Answer, Quiz
from django.views.generic import DetailView, ListView, CreateView
from domecode.mixins import PageTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class QuizHomeView(PageTitleMixin, ListView):
    model = Ques
    template_name = "quizzes/quiz_home.html"
    context_object_name = "ques"
    title = 'Quizzes'

class QuizDetailView(PageTitleMixin, DetailView):
    model = Quiz
    template_name = "quizzes/quiz_detail.html"
    context_object_name = "ques"
    title = 'Quizzes - List'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['ques'] = instance.ques_set.filter(Language="PYTHON")
        return context


class QuesDetailView(PageTitleMixin,LoginRequiredMixin, DetailView):
    model = Ques
    title = 'Quiz Question'
    template_name = "quizzes/ques_detail.html"


class AnswerCreateView(PageTitleMixin,LoginRequiredMixin, CreateView):
    model = Answer
    title = 'Attempt Question'
    fields = ['answer']

    def get_success_url(self):
        question = self.object.question
        return reverse('quizzes:detail', kwargs={'slug': question.slug})

    def form_valid(self, form):
        form.instance.user = self.request.user
        question = Ques.objects.get(slug=self.kwargs['qslug'])

        form.instance.question = question

        if form.instance.answer == question.solution:
            form.instance.iscorrect = True

        if form.instance.iscorrect:
            if form.instance.question.quiz.typeof == "EASY":
                form.instance.user.profile.domes += 2
            if form.instance.question.quiz.typeof == "MEDIUM":
                form.instance.user.profile.domes += 4
            if form.instance.question.quiz.typeof == "HARD":
                form.instance.user.profile.domes += 10

        form.instance.user.profile.save()
        form.save()

        return super().form_valid(form)
