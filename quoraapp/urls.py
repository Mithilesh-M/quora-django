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
]
