from django.db import models

# Create your models here.

class Faq(models.Model):
    title = models.CharField(max_length = 120, verbose_name = "Başlıq")
    content = models.CharField(max_length = 200, verbose_name = "Məzmun")
