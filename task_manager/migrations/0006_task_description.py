# Generated by Django 4.1.4 on 2023-01-16 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0005_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=700),
        ),
    ]