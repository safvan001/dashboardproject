from django.db import models

# Create your models here.
# dashboard_app/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class Reminder(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField()

    def __str__(self):
        return self.name
