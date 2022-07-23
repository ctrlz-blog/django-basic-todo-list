import datetime

from django.db.models import QuerySet
from django.http import HttpResponse
from django.urls import reverse
from django.test import TestCase, Client

from todo.models import Task


class TestTaskModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Creates a task instance that our tests can access.
        setUpTestData is executed once, so our task instance is
        shared between tests.
        """
        cls.task_name = "Book dentist appointment"
        cls.task = Task.objects.create(name=cls.task_name)

    def test_task_name(self):
        self.assertEqual(self.task.name, self.task_name)

    def test_task_default_status(self):
        """Test that our task was assigned a status of 'To Do'"""

        expected = Task.StatusChoice.TODO
        actual = self.task.status

        self.assertEqual(expected, actual)

    def test_task_created(self):
        """Tests that task.created stores a datetime"""

        self.assertEqual(type(self.task.created), datetime.datetime)

    def test_str(self):
        expected = f"To Do: {self.task_name}"
        actual = str(self.task)

        self.assertEqual(expected, actual)


class TestIndexView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("index")
        cls.client = Client()
        cls.task = Task.objects.create(name="book dentist appointment")

    def test_index_view_returns_httpresponse(self):
        """Test our view returns a HttpResponse"""

        response = self.client.get(self.url)

        self.assertTrue(isinstance(response, HttpResponse))

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        """Tests the context contains queryset of tasks"""
        response = self.client.get(self.url)

        self.assertIn("tasks", response.context)

        tasks = response.context["tasks"]

        self.assertTrue(isinstance(tasks, QuerySet))
        self.assertEqual(tasks.first(), self.task)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "temp_index.html")


from todo.forms import TaskForm


class TestTaskForm(TestCase):
    def test_form_instance(self):
        """Test that form has name field"""
        form = TaskForm()

        self.assertIn("name", form.fields)

    def test_is_valid(self):
        form = TaskForm(data={"name": "Book dentist appointment"})

        self.assertTrue(form.is_valid())

    def test_empty_form_invalid(self):
        form = TaskForm(data={"name": None})

        self.assertFalse(form.is_valid())
