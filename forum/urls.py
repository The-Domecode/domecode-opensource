from django.urls import path
from .import views
from .views import (QueryCreateView, QueryListView, QueryUpdateView, QueryDeleteView, QueryDetailView, QueryLikeAPIToggle, QueryLikeToggle,
                    AnswerCreateView, AnswerDeleteView, AnswerUpdateView, AnswerDetailView, AcceptAnswerView, CommentCreateView, CommentDeleteView, CommentUpdateView, )

app_name = 'forum'

urlpatterns = [
    # forum url
    path('forum/', QueryListView.as_view(), name='list'),
    path('forum/guidelines', views.guidelines, name='guidelines'),
    # query urls
    path('forum/query/new/', QueryCreateView.as_view(), name='query-create'),
    path('forum/query/<slug:slug>/', QueryDetailView.as_view(), name='detail'),
    path('forum/query/<slug:slug>/update/',
         QueryUpdateView.as_view(), name='query-update'),
    path('forum/query/<slug:slug>/delete/',
         QueryDeleteView.as_view(), name='query-delete'),
    path('forum/query/<slug:slug>/like/',
         QueryLikeToggle.as_view(), name='query-likes-toggle'),
    path('api/forum/query/<slug:slug>/like/',
         QueryLikeAPIToggle.as_view(), name='query-likes-api-toggle'),

    # answer urls

    path('forum/query/<slug:qslug>/answer/create/',
         AnswerCreateView.as_view(), name='answer-create'),
    path('forum/query/<slug:qslug>/answer/<slug:slug>/',
         AnswerDetailView.as_view(), name='answer-detail'),
    path('forum/query/<slug:qslug>/answer/update/<slug:slug>',
         AnswerUpdateView.as_view(), name='answer-update'),
    path('forum/query/<slug:qslug>/answer/delete/<slug:slug>/',
         AnswerDeleteView.as_view(), name='answer-delete'),
    path('forum/query/<slug:qslug>/answer/accept/<slug:slug>/',
         AcceptAnswerView.as_view(), name='accept'),
    # commenturls
    path('forum/query/<slug:qslug>/answer/<slug:aslug>/comment/create/',
         CommentCreateView.as_view(), name='comment-create'),
    path('forum/query/<slug:qslug>/answer/<slug:aslug>/comment/update/<slug:slug>',
         CommentUpdateView.as_view(), name='comment-update'),
    path('forum/query/<slug:qslug>/answer/<slug:aslug>/comment/delete/<slug:slug>/',
         CommentDeleteView.as_view(), name='comment-delete'),
    # path('forum/query/<slug:qslug>/answer/like/',
    #     AnswerLikeToggle.as_view(), name='answer-likes-toggle'),
    #  path('api/forum/answer/<slug:slug>/like/',
    #      AnswerLikeAPIToggle.as_view(), name='answer-likes-api-toggle'),
]
