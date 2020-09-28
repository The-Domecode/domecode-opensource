from django.test import TestCase
from .models import Question, Answer
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.


def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    user.save()
    return user


def create_question(language="PYTHON"):
    with open("coder/testfiles/output.txt") as file:
        f = SimpleUploadedFile("normal.txt", str.encode(file.read()))
    question = Question(title="Test",
                        content="Test",
                        solution=f,
                        typeof=language)
    question.save()
    return question


class CoderCreateViewTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_correct_answer_works_python(self):
        """
        Check if checking works correctly for python program
        """
        create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        ques1 = create_question("PYTHON")
        with open("coder/testfiles/normal.py") as f:
            self.client.post(
                reverse("coder:submit", kwargs={"qslug": ques1.slug}),
                data={
                    "language": "PYTHON",
                    "result": f
                },
            )
        self.assertTrue(Answer.objects.all()[0].iscorrect)

    def test_correct_answer_works_java(self):
        """
        Check if checking works correctly for java program
        """
        create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        ques1 = create_question()
        with open("coder/testfiles/normal.java") as f:
            self.client.post(
                reverse("coder:submit", kwargs={"qslug": ques1.slug}),
                data={
                    "language": "JAVA",
                    "result": f
                },
            )
        self.assertTrue(Answer.objects.all()[0].iscorrect)

    def test_correct_answer_works_cpp(self):
        """
        Check if checking works correctly for c++ program
        """
        create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        ques1 = create_question()
        with open("coder/testfiles/normal.cpp") as f:
            self.client.post(
                reverse("coder:submit", kwargs={"qslug": ques1.slug}),
                data={
                    "language": "C++",
                    "result": f
                },
            )
        self.assertTrue(Answer.objects.all()[0].iscorrect)

    def test_correct_answer_works_rust(self):
        """
        Check if checking works correctly for rust program
        """
        create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        ques1 = create_question()
        with open("coder/testfiles/normal.rs") as f:
            self.client.post(
                reverse("coder:submit", kwargs={"qslug": ques1.slug}),
                data={
                    "language": "RUST",
                    "result": f
                },
            )
        self.assertTrue(Answer.objects.all()[0].iscorrect)

    def test_correct_answer_works_go(self):
        """
        Check if checking works correctly for rust program
        """
        create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        ques1 = create_question()
        with open("coder/testfiles/normal.go") as f:
            self.client.post(
                reverse("coder:submit", kwargs={"qslug": ques1.slug}),
                data={
                    "language": "GO",
                    "result": f
                },
            )
        self.assertTrue(Answer.objects.all()[0].iscorrect)

    def test_correct_answer_works_c(self):
        """
        Check if checking works correctly for rust program
        """
        create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        ques1 = create_question()
        with open("coder/testfiles/normal.c") as f:
            self.client.post(
                reverse("coder:submit", kwargs={"qslug": ques1.slug}),
                data={
                    "language": "C",
                    "result": f
                },
            )
        self.assertTrue(Answer.objects.all()[0].iscorrect)

    def test_multiple_correct_answers_increase_domes_once(self):
        """
        Even if the user submits the answer after having solved the question once
        their points shouldn't increase
        """
        user = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        ques1 = create_question("PYTHON")
        with open("coder/testfiles/normal.java") as f:
            self.client.post(
                reverse("coder:submit", kwargs={"qslug": ques1.slug}),
                data={
                    "language": "PYTHON",
                    "result": f
                },
            )
        user.refresh_from_db()
        self.assertEqual(user.profile.domes, 0)

        with open("coder/testfiles/normal.py") as f:
            self.client.post(
                reverse("coder:submit", kwargs={"qslug": ques1.slug}),
                data={
                    "language": "PYTHON",
                    "result": f
                },
            )

            self.client.post(
                reverse("coder:submit", kwargs={"qslug": ques1.slug}),
                data={
                    "language": "PYTHON",
                    "result": f
                },
            )  # Post the correct answer twice
        user.refresh_from_db()
        self.assertEqual(user.profile.domes, 15)
