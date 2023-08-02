from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.CharField(max_length=100)
    date = models.DateField()
    datedue = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title
