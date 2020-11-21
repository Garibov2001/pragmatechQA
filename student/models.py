from django.db import models
from django.utils import timezone


class Group(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    avatar_path = models.CharField(max_length=255)
    group = models.ForeignKey(Group ,related_name='students', on_delete = models.PROTECT)


class Actions(models.Model):
    student = models.ForeignKey(Student, related_name='actions', on_delete = models.PROTECT) 
    question = models.CharField(max_length=255) #Burada foreign key olacaq 
    reply_date = models.DateTimeField(default = timezone.now)
    action_type = models.BooleanField()  # False - 'Downvote', True - 'Upvote',  