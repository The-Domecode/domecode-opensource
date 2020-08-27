from django.urls import path
from .views import AnswerCreateView, QuesDetailView, QuizDetailView, QuizHomeView
app_name = 'quizzes'

urlpatterns = [
    path('', QuizHomeView.as_view(), name='home'),
    path('python/<slug:slug>', QuizDetailView.as_view(), name='detail-python'),
    path('question/<slug:slug>', QuesDetailView.as_view(), name='detail'),
    path('<slug:qslug>/answer/', AnswerCreateView.as_view(), name='submit')
]
