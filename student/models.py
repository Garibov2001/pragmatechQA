from django.db import models
from django.utils import timezone


class Group(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.

class category(models.Model):
    """Model definition for category."""

    name = models.CharField(verbose_name=("Ad"), max_length=50)

    description = models.TextField(verbose_name=("Açıqlama"))

    class Meta:
        """Meta definition for category."""

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        """Unicode representation of category."""
        return self.name


class question(models.Model):
    """Model definition for question."""

    title = models.CharField(verbose_name=("Başlıq"), max_length=50)
    category = models.ManyToManyField("category", verbose_name=("Kategoriya"))
    content = models.TextField(verbose_name=("Kontent"))


    class Meta:
        """Meta definition for question."""

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
    student = models.ForeignKey(Student, related_name='actions', on_delete = models.PROTECT) 
    question = models.CharField(max_length=255) #Burada foreign key olacaq 
    reply_date = models.DateTimeField(default = timezone.now)
    action_type = models.BooleanField()  # False - 'Downvote', True - 'Upvote',  

