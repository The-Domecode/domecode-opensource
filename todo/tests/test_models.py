from todo.models import Todo
from django.contrib.auth.models import User
from django.test import TestCase
from model_bakery import baker


def createCustomUser():
    return User.objects.create(username="Test")


class TestModels(TestCase):
    def test_event_model(self):
        task = baker.make(Todo, title="Sum2Prove")
        self.assertEqual(str(task), "Sum2Prove")

    def test_event_model_two(self):
        task = baker.make(Todo, title="Sum2Prove")
        self.assertEqual(str(task), "Sum2Prove")
