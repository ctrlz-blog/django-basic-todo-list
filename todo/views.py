from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseRedirect,
)
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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


def update_task_status(
    request: HttpRequest, task_id: int, new_status: str
) -> HttpResponse:

    if not new_status in Task.StatusChoice.values:
        return HttpResponseBadRequest("Invalid status")

    task = get_object_or_404(Task, id=task_id)

    task.status = new_status
    task.save()

    success_url = reverse("index")

    return HttpResponseRedirect(success_url)


def delete_task(request: HttpRequest, task_id: int) -> HttpResponse:

    task = get_object_or_404(Task, id=task_id)
    task.delete()

    success_url = reverse("index")

    return HttpResponseRedirect(success_url)
