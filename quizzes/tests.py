from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Quiz, Ques, Answer
from django.contrib.auth.models import User

# Create your tests here.


def create_quiz(name, Language="python", typeof="EASY"):
    quiz = Quiz(name=name, Language=Language, typeof=typeof)
    quiz.save()
    return quiz


def create_ques(title, quiz, solution="A"):
    ques = Ques(title=title, quiz=quiz, solution=solution)
    ques.save()
    return ques


def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    user.save()
    return user


class QuizHomeViewTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_home_renders_correctly(self):
        """
        Home page should load
        """
        create_quiz("TestQuiz")
        response = self.client.get(reverse("quizzes:home"))
        self.assertContains(response, "TestQuiz")


class QuizDetailsViewTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_list_view_works_correctly(self):
        """
        The view must contain the ques in the created quiz and none of the questions of other quizzes
        """
        quiz1 = create_quiz("TestQuiz1")
        quiz2 = create_quiz("TestQuiz2")
        create_ques(title="TestQues1", quiz=quiz1)
        create_ques(title="TestQues2", quiz=quiz1)
        create_ques(title="TestQues3", quiz=quiz2)
        response = self.client.get(
            reverse("quizzes:detail-python", kwargs={"slug": quiz1.slug})
        )
        self.assertContains(response, "TestQues1")
        self.assertContains(response, "TestQues2")
        self.assertNotContains(response, "TestQues3")


class QuesDetailsViewTesst(TestCase):
    def setup(self):
        self.client = Client()

    def test_unauthenticated_user_cannot_view_ques(self):
        """
        Unauthenticated user shouldn't be able to view
        """
        quiz = create_quiz("TestQuiz")
        ques = create_ques(title="TestQues", quiz=quiz)
        response = self.client.get(
            reverse("quizzes:detail", kwargs={"slug": ques.slug}), follow=True
        )
        self.assertNotContains(response, "TestQues")

    def test_authenticated_user_can_view_the_ques(self):
        """
        Ques should render correctly for authed user.
        """
        create_user(username="TestUser", password="test000")
        self.client.login(username="TestUser", password="test000")
        quiz = create_quiz("TestQuiz")
        ques = create_ques(title="TestQues", quiz=quiz)
        response = self.client.get(
            reverse("quizzes:detail", kwargs={"slug": ques.slug})
        )
        self.assertContains(response, "TestQues")


class AnswerCreateViewTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_answer_create_view_works_correctly_easy(self):
        """
        On creating an answer the domes of the user must update correctly for easy quiz
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        quiz = create_quiz("TestQuiz")
        ques1 = create_ques(title="TestQues1", quiz=quiz, solution="B")
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "A"},
        )
        user1.refresh_from_db()
        self.assertEquals(
            Answer.objects.filter(question=ques1)
            .filter(user=user1)
            .filter(iscorrect=True)
            .count(),
            0,
        )
        self.assertEquals(user1.profile.domes, 0)
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "B"},
        )
        user1.refresh_from_db()
        self.assertEquals(
            Answer.objects.filter(question=ques1)
            .filter(user=user1)
            .filter(iscorrect=True)
            .count(),
            1,
        )
        self.assertEquals(user1.profile.domes, 2)
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "B"},
        )
        user1.refresh_from_db()
        self.assertEquals(
            Answer.objects.filter(question=ques1)
            .filter(user=user1)
            .filter(iscorrect=True)
            .count(),
            2,
        )
        self.assertEquals(user1.profile.domes, 2)

    def test_answer_create_view_works_correctly_medium(self):
        """
        On creating an answer the domes of the user must update correctly for easy quiz
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        quiz = create_quiz("TestQuiz", typeof="MEDIUM")
        ques1 = create_ques(title="TestQues1", quiz=quiz, solution="B")
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "A"},
        )
        user1.refresh_from_db()
        self.assertEquals(user1.profile.domes, 0)
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "B"},
        )
        user1.refresh_from_db()
        self.assertEquals(user1.profile.domes, 4)
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "B"},
        )
        user1.refresh_from_db()
        self.assertEquals(user1.profile.domes, 4)

    def test_answer_create_view_works_correctly_hard(self):
        """
        On creating an answer the domes of the user must update correctly for easy quiz
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        quiz = create_quiz("TestQuiz", typeof="HARD")
        ques1 = create_ques(title="TestQues1", quiz=quiz, solution="B")
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "A"},
        )
        user1.refresh_from_db()
        self.assertEquals(user1.profile.domes, 0)
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "B"},
        )
        user1.refresh_from_db()
        self.assertEquals(user1.profile.domes, 10)
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "B"},
        )
        user1.refresh_from_db()
        self.assertEquals(user1.profile.domes, 10)

    def test_answer_create_view_for_multiple_ques_works_correctly(self):
        """
        On creating an answer the domes of the user must update correctly for easy quiz
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        quiz = create_quiz("TestQuiz")
        ques1 = create_ques(title="TestQues1", quiz=quiz, solution="B")
        ques2 = create_ques(title="TestQues2", quiz=quiz, solution="B")
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques1.slug}),
            data={"answer": "B"},
        )
        user1.refresh_from_db()
        self.assertEquals(
            Answer.objects.filter(question=ques1)
            .filter(user=user1)
            .filter(iscorrect=True)
            .count(),
            1,
        )
        self.assertEquals(user1.profile.domes, 2)
        self.client.post(
            reverse("quizzes:submit", kwargs={"qslug": ques2.slug}),
            data={"answer": "B"},
        )
        user1.refresh_from_db()
        self.assertEquals(
            Answer.objects.filter(question=ques2)
            .filter(user=user1)
            .filter(iscorrect=True)
            .count(),
            1,
        )
        self.assertEquals(user1.profile.domes, 4)
