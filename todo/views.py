from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from todo.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by("-created")

    context = {"tasks": tasks}

    return render(request, "temp_index.html", context)
