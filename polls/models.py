from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
# 在这个简单的投票应用中，需要创建两个模型：问题 Question 和选项 Choice。
# Question 模型包括问题描述和发布时间。
# Choice 模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # 这是个演示方法，调用这个方法为了判断某个问题是不是最近的时间发表的
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 我们使用 ForeignKey 定义了一个关系。这将告诉 Django，每个 Choice 对象都关联到一个 Question 对象。
    # Django 支持所有常用的数据库关系：多对一、多对多和一对一。
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
