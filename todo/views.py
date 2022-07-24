from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from todo.forms import TaskForm
from todo.models import Task


def index(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()

    form = TaskForm()
    tasks = Task.objects.all().order_by("-created")

    context = {"tasks": tasks, "form": form, "Status": Task.StatusChoice}

    return render(request, "index.html", context)
