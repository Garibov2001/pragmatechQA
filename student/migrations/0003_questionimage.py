# Generated by Django 3.1.3 on 2020-11-29 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_delete_questionimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='question_images/', verbose_name='Sualın şəkli')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.question')),
            ],
            options={
                'verbose_name': 'QuestionImage',
                'verbose_name_plural': 'QuestionImage',
            },
        ),
    ]
