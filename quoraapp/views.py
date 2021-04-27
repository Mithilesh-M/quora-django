from django.shortcuts import render
from .models import Question, Answer, Comment
from django.contrib.auth.models import User
from django_filters import views
from .filters import QuestionFilter
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


def show_index(request):
    context = {
        'No_Of_Question': Question.objects.all().count(),
        'No_Of_Answer': Answer.objects.all().count(),
        'No_Of_Comment': Comment.objects.all().count(),
        'No_Of_User': User.objects.all().count(),
    }
    return render(request, 'quoraapp/index.html', context)


class UserCreateView(generic.CreateView):
    model = get_user_model()
    fields = ('username', 'first_name', 'last_name', 'email', 'password')
    template_name = 'quoraapp/user_form.html'
    success_url = reverse_lazy('question-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        self.success_url = reverse('index')
        return super(UserCreateView, self).form_valid(form)


class QuestionListView(views.FilterView):
    filterset_class = QuestionFilter
    template_name = 'quoraapp/question_list.html'


class QuestionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Question
    fields = ['title', 'description', 'tags', 'vote']
    success_url = reverse_lazy('question-list')

    def form_valid(self, form):
        question = form.save(commit=False)
        question.user = User.objects.get(pk=self.request.user.id)
        question.save()
        self.success_url = reverse('question-list')
        return super(QuestionCreateView, self).form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Question
    fields = ['title', 'description', 'tags', 'vote']

    def get_success_url(self):
        return reverse_lazy('question-detail', kwargs={'pk': self.kwargs['pk']})


class QuestionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Question
    success_url = reverse_lazy('question-list')


class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = Question.objects.get(pk=self.kwargs.get('pk'))
        answer = question.answer_set.all()
        context['answer_list'] = answer
        return context


class AnswerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Answer
    fields = ['answer', 'vote']

    def get_success_url(self):
        answer_id = self.kwargs['pk']
        question = Answer.objects.get(pk=answer_id).question
        return reverse_lazy('question-detail', kwargs={'pk': question.id})


class AnswerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Answer

    def get_success_url(self):
        answer_id = self.object.id
        question = Answer.objects.get(pk=answer_id).question
        return reverse_lazy('question-detail', kwargs={'pk': question.id})


class AnswerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Answer
    fields = ['answer', 'vote']

    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.user = User.objects.get(pk=self.request.user.id)
        answer.question = Question.objects.get(pk=self.kwargs['pk'])
        answer.save()
        self.success_url = reverse('question-detail', kwargs={'pk': answer.question.id})
        return super(AnswerCreateView, self).form_valid(form)


class CommentCreateViewQuestion(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ['comment', 'vote']

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = User.objects.get(pk=self.request.user.id)
        comment.question = Question.objects.get(pk=self.kwargs['pk'])
        comment.save()
        self.success_url = reverse('question-detail', kwargs={'pk': comment.question.id})
        return super(CommentCreateViewQuestion, self).form_valid(form)


class CommentDeleteViewQuestion(LoginRequiredMixin, generic.DeleteView):
    model = Comment

    def get_success_url(self):
        comment_id = self.object.id
        question = Comment.objects.get(pk=comment_id).question
        return reverse_lazy('question-detail', kwargs={'pk': question.id})


class CommentUpdateViewQuestion(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    fields = ['comment', 'vote']

    def get_success_url(self):
        comment_id = self.object.id
        question = Comment.objects.get(pk=comment_id).question
        return reverse_lazy('question-detail', kwargs={'pk': question.id})


class CommentCreateViewAnswer(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ['comment', 'vote']

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = User.objects.get(pk=self.request.user.id)
        comment.answer = Answer.objects.get(pk=self.kwargs['pk'])
        comment.save()
        self.success_url = reverse('question-detail', kwargs={'pk': comment.answer.question.id})
        return super(CommentCreateViewAnswer, self).form_valid(form)


class CommentDeleteViewAnswer(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    success_url = reverse_lazy('question-list')

    def get_success_url(self):
        comment_id = self.object.id
        question = Comment.objects.get(pk=comment_id).answer.question
        return reverse_lazy('question-detail', kwargs={'pk': question.id})


class CommentUpdateViewAnswer(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    fields = ['comment', 'vote']
    success_url = reverse_lazy('question-list')

    def get_success_url(self):
        comment_id = self.object.id
        question = Comment.objects.get(pk=comment_id).answer.question
        return reverse_lazy('question-detail', kwargs={'pk': question.id})
