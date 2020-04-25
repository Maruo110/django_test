from django.db import models


class Question(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
