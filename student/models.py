from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Group(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.

class Setting(models.Model):
    communityRules = models.CharField(max_length = 255, name="cRules")


class Faq(models.Model):
    title = models.CharField(max_length = 120, verbose_name = "Başlıq")
    content = models.CharField(max_length = 200, verbose_name = "Məzmun")

class Question(models.Model):
    """Model definition for Question."""

    title = models.CharField(verbose_name=("Başlıq"), max_length=50)
    tags = TaggableManager()
    content = models.TextField(verbose_name=("Kontent"))


    class Meta:
        """Meta definition for Question."""

        verbose_name = 'question'
        verbose_name_plural = 'questions'

    def __str__(self):
        """Unicode representation of question."""
        return self.title
    

class Student(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    avatar_path = models.CharField(max_length=255)
    group = models.ForeignKey(Group ,related_name='students', on_delete = models.PROTECT)


class Actions(models.Model):
    student = models.ForeignKey(Student, related_name='actions', on_delete = models.CASCADE) 
    question = models.CharField(max_length=255) #Burada foreign key olacaq 
    reply_date = models.DateTimeField(default = timezone.now)
    action_type = models.BooleanField()  # False - 'Downvote', True - 'Upvote',  


