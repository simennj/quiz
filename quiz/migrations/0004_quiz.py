# Generated by Django 2.0 on 2017-12-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('quiz', '0003_answer_answered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('name', models.SlugField(max_length=16, primary_key=True, serialize=False)),
                ('questions', models.ManyToManyField(to='quiz.Question')),
            ],
        ),
    ]
