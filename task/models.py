from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create Task model

class Task(models.Model):
    tasktitle = models.CharField(max_length=150)
    taskdetail = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tasktitle

class Num(models.Model):
    number = models.IntegerField()

    def ___str__(self):
        return self.number

    

