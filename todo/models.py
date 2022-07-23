from django.db import models


class Task(models.Model):
    class StatusChoice(models.TextChoices):
        TODO = "To Do"
        DOING = "Doing"
        DONE = "Done"

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=StatusChoice.choices, max_length=100, default=StatusChoice.TODO
    )

    def __str__(self):
        """Provides a readable reference for each object"""
        return f"{self.status}: {self.name}"
