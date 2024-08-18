from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    password = models.TextField()

    def __str__(self):
        return f"Email: {self.email}, Password: {self.password}"

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    due_by = models.DateTimeField(default=datetime.now())
    priority = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(3)])
    is_urgent = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task name: {self.task_name}, Due by: {self.due_by}, Priority: {self.priority}, Is Urgent?: {self.is_urgent}"