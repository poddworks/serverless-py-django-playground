import datetime

from django.db import models
from django.utils import timezone


def make_filename(inst, filename):
    return f'{filename}_{int(timezone.now().timestamp() * 1000)}'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_icon = models.FileField(max_length=200, default='null.ico', upload_to=make_filename)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
