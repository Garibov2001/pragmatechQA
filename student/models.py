from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class StudyGroup(models.Model):
    """Model definition for Group."""
    name = models.CharField(verbose_name=("Ad"), max_length=255)

    class Meta:
        """Meta definition for Group."""

        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        """Unicode representation of Group."""
        return self.name


class Student(models.Model):
    """Model definition for Student."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    picture = models.ImageField(verbose_name=("Şəkil"), upload_to='static/images/profile_images')
    study_group = models.ForeignKey(StudyGroup ,verbose_name=("Qrup"), on_delete = models.PROTECT)

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        return self.name + " " + self.surname


class Setting(models.Model):
    """Model definition for Setting."""

    communityRules = models.TextField(verbose_name="Qaydalar")

    class Meta:
        """Meta definition for Setting."""

        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self):
        """Unicode representation of Setting."""
        return self.communityRules


class FAQ(models.Model):
    """Model definition for FAQ."""

    title = models.CharField(verbose_name = "Başlıq", max_length = 255)
    content = models.TextField(verbose_name = "Məzmun")

    class Meta:
        """Meta definition for FAQ."""

        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self):
        """Unicode representation of FAQ."""
        return self.title


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(verbose_name="Ad", max_length=50)
    description = models.TextField(verbose_name="Məzmun")

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Question(models.Model):
    """Model definition for Question."""

    title = models.CharField(verbose_name="Başlıq", max_length=50)
    category = models.ManyToManyField("Category", verbose_name="Kategoriyalar")
    content = models.TextField(verbose_name="Məzmun")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return self.title


class Comment(models.Model):
    """Model definition for Comment."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name=("Məzmun"), null=True)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return self.comment


class Action(models.Model):
    """Model definition for Action."""

    student = models.ForeignKey(Student, verbose_name="Tələbə", on_delete = models.PROTECT) 
    question = models.ForeignKey(Question, verbose_name="Sual", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, verbose_name="Komment", on_delete=models.CASCADE)
    type = models.BooleanField(verbose_name=("Tip"))
    reply_date = models.DateTimeField(default = timezone.now)
    action_type = models.BooleanField()  # False - 'Downvote', True - 'Upvote',

    class Meta:
        """Meta definition for Action."""

        verbose_name = 'Action'
        verbose_name_plural = 'Actions'

    def __str__(self):
        """Unicode representation of Action."""
        return self.action_type