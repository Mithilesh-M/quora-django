import django_filters
from .models import Question, Answer, Comment

class QuestionFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    description = django_filters.CharFilter(lookup_expr='icontains', label='Description')

    class Meta:
        model = Question
        fields = ['title', 'user', 'description', 'vote']
