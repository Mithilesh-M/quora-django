from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Question(models.Model):
    """Model representing a Question."""
    title = models.CharField(max_length=200, help_text='Enter question title')
    description = models.TextField(max_length=700, help_text='Enter question description')
    tags = TaggableManager(help_text='Enter question tags')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    VOTE = (
        ('u', 'Up-vote'),
        ('d', 'Down-vote'),
        ('n', 'None'),
    )
    vote = models.CharField(
        max_length=1,
        choices=VOTE,
        blank=False,
        default='n',
        help_text='Enter Vote',
    )


class Answer(models.Model):
    """Model representing a Answer."""
    answer = models.TextField(max_length=1000, help_text='Enter answer for question')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    VOTE = (
        ('u', 'Up-vote'),
        ('d', 'Down-vote'),
        ('n', 'None'),
    )
    vote = models.CharField(
        max_length=1,
        choices=VOTE,
        blank=False,
        default='n',
        help_text='Enter Vote',
    )


class Comment(models.Model):
    """Model representing a Comment."""
    comment = models.TextField(max_length=1000, help_text='Enter comment')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    VOTE = (
        ('u', 'Up-vote'),
        ('d', 'Down-vote'),
        ('n', 'None'),
    )
    vote = models.CharField(
        max_length=1,
        choices=VOTE,
        blank=False,
        default='n',
        help_text='Enter Vote',
    )
