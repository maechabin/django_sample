import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    # CharField では max_length が必須
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # オブジェクトを文字列に変換して返す
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # リレーションシップの定義
    # それぞれの Choice が一つの Question に関連付けられることを Django に伝える
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # CharField では max_length が必須
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
