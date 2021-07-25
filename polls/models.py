from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    create_at = models.DateTimeField('date published', auto_now_add=True)
    updated_at = models.DateField('date updated', auto_now=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)