from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('question/', views.QuestionListView.as_view(), name='question-list'),
    path('question/create', views.QuestionCreateView.as_view(), name='question-create'),
    path('question/update/<int:pk>', views.QuestionUpdateView.as_view(), name='question-update'),
    path('question/delete/<int:pk>', views.QuestionDeleteView.as_view(), name='question-delete'),
    path('question/detail/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('answer/update/<int:pk>', views.AnswerUpdateView.as_view(), name='answer-update'),
    path('answer/delete/<int:pk>', views.AnswerDeleteView.as_view(), name='answer-delete'),
    path('answer/create/question/<int:pk>', views.AnswerCreateView.as_view(), name='answer-create'),
    path('comment-question/create/question/<int:pk>', views.CommentCreateViewQuestion.as_view(), name='comment-question-create'),
    path('comment-question/delete/<int:pk>', views.CommentDeleteViewQuestion.as_view(), name='comment-question-delete'),
    path('comment-question/update/<int:pk>', views.CommentUpdateViewQuestion.as_view(), name='comment-question-update'),
    path('comment-answer/create/answer/<int:pk>', views.CommentCreateViewAnswer.as_view(), name='comment-answer-create'),
    path('comment-answer/delete/<int:pk>', views.CommentDeleteViewAnswer.as_view(), name='comment-answer-delete'),
    path('comment-answer/update/<int:pk>', views.CommentUpdateViewAnswer.as_view(), name='comment-answer-update'),
    path('register/', views.UserCreateView.as_view(), name="register"),
]
