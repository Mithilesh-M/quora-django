from django.shortcuts import render
from .models import Question, Answer, Comment
from django.contrib.auth.models import User
from django_filters import views
from .filters import QuestionFilter
from django.views import generic
from django.urls import reverse_lazy


def show_index(request):
    context = {
        'No_Of_Question': Question.objects.all().count(),
        'No_Of_Answer': Answer.objects.all().count(),
        'No_Of_Comment': Comment.objects.all().count(),
        'No_Of_User': User.objects.all().count(),
    }
    return render(request, 'quoraapp/index.html', context)


class QuestionListView(views.FilterView):
    filterset_class = QuestionFilter
    template_name = 'quoraapp/question_list.html'


class QuestionCreateView(generic.CreateView):
    model = Question
    fields = ['title', 'user', 'description', 'tags']
    success_url = reverse_lazy('question-list')
