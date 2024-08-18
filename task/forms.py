from django import forms

from .models import Task 

class CreateNewTask(forms.Form):
    task_name = forms.CharField(label="Task Name", max_length=200)
    due_by = forms.DateTimeField(label="Due Date", widget=
                                 forms.DateInput(
                                     attrs={
                                         'class': 'form-control',
                                         'type': 'datetime-local'
                                     }
                                 ))
    priority = forms.IntegerField(min_value=1, max_value=3, label="Priority (High = 1, Low = 3)")
    is_urgent = forms.BooleanField(label="Urgent?", required=False)