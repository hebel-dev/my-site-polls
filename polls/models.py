from django.db import models
import datetime
from django.utils import timezone 


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    create_at = models.DateTimeField('date published', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.create_at >= timezone.now() - datetime.timedelta(days = 1)   

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question} : {self.choice_text}'