# Generated by Django 4.2.5 on 2023-09-06 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
    ]