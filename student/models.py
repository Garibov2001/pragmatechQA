from django.db import models

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