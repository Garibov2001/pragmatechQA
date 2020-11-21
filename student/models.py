from django.db import models

# Create your models here.

class Setting(models.Model):
    communityRules = models.CharField(max_length = 255, name="cRules")


class Faq(models.Model):
    title = models.CharField(max_length = 120, verbose_name = "Başlıq")
    content = models.CharField(max_length = 200, verbose_name = "Məzmun")


