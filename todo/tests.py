import datetime

from django.test import TestCase

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
