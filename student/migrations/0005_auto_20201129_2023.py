# Generated by Django 3.1.3 on 2020-11-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20201129_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionimage',
            name='image',
            field=models.ImageField(upload_to='question_images', verbose_name='Sualın şəkli'),
        ),
    ]
