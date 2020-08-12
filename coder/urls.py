from django.urls import path
from .import views
from .views import CoderListViewPy, CoderListViewJava, CoderListViewGen, CoderDetailView, CoderCreateView, SubmissionListView
app_name = 'coder'

urlpatterns = [
    path('', views.coderhome, name='home'),
    path('python/', CoderListViewPy.as_view(), name='list-python'),
    path('java/', CoderListViewJava.as_view(), name='list-java'),
    path('general/', CoderListViewGen.as_view(), name='list-general'),
    path('question/<slug:slug>/', CoderDetailView.as_view(), name='detail'),
    path('submissions', SubmissionListView.as_view(), name='submissions'),
    path('<slug:qslug>/answer/', CoderCreateView.as_view(), name='submit')
]
