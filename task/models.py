from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    task_name = models.CharField(max_length=200)
    due_by = models.DateTimeField(default=datetime.now())
    priority = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(3)])
    is_urgent = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task name: {self.task_name}, Due by: {self.due_by}, Priority: {self.priority}, Is Urgent?: {self.is_urgent}"