from django.test import TestCase

# Create your tests here.

from .models import Todo
from django.test import TestCase
from django.urls import reverse  # new
from rest_framework import status  # new
from rest_framework.test import APITestCase  # new


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="This is test title", body="This is test body"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "This is test title")
        self.assertEqual(self.todo.body, "This is test body")
        self.assertEqual(str(self.todo), "This is test title")

    def test_api_listview(self):  # new
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):  # new
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First Todo")
