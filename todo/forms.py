from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name"]

    name = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                "aria-label": "name",
                "placeholder": "What do you need to do?",
                "class": "form-control form-control-lg inline-block",
            }
        ),
    )
