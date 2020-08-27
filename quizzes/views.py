from .models import Ques, Answer, Quiz
from django.views.generic import DetailView, ListView, CreateView
from domecode.mixins import PageTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class QuizHomeView(PageTitleMixin, ListView):
    model = Quiz
    template_name = "quizzes/quiz_home.html"
    context_object_name = "quiz"
    title = 'Quizzes'


"""
Quiz Detail View is the detail of a quiz wherein the context_data method helps
 return the questions for that particular quiz.
There's a reason behind why the filter==Python got removed and .all() got
placed instead.
In order to return the questions for a particular quiz there were two options :

A. Since both quiz and ques have a language attribute, we could have a quiz in
 any language, have ques in various languages. do manipulation in quiz home
template and create separate templates for different language quizzes. Pros :
 Single Detail View, CONS : Too much HTML to deal with.

B. Minimal manipulation in HTML, single detail view template.
Pros : Single template,
Single View CONS : A quiz with a specified language can't
have questions of other languages. Not technically a con but yeah,
something to take note of.
"""


class QuizDetailView(PageTitleMixin, DetailView):
    model = Quiz
    template_name = "quizzes/quiz_detail.html"
    context_object_name = "ques"
    title = 'Quizzes - List'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['ques'] = instance.ques_set.all()
        return context


# TODO: Can remove LoginRequiredMixin
class QuesDetailView(PageTitleMixin, LoginRequiredMixin, DetailView):
    model = Ques
    title = 'Quiz Question'
    template_name = "quizzes/ques_detail.html"


class AnswerCreateView(PageTitleMixin, LoginRequiredMixin, CreateView):
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

        if form.instance.iscorrect and Answer.objects.filter(question=question).filter(user=form.instance.user).filter(iscorrect=True).count() == 0:
            if form.instance.question.quiz.typeof == "EASY":
                form.instance.user.profile.domes += 2
            if form.instance.question.quiz.typeof == "MEDIUM":
                form.instance.user.profile.domes += 4
            if form.instance.question.quiz.typeof == "HARD":
                form.instance.user.profile.domes += 10

        form.instance.user.profile.save()
        form.save()

        return super().form_valid(form)
