from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name"]
