from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('question/', views.QuestionListView.as_view(), name='question-list'),
]