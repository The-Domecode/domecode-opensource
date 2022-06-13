from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Notes
from django.contrib.auth.models import User

# Create your tests here.


def create_note(title, user):
    note = Notes(title=title, user=user)
    note.save()
    return note


def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    user.save()
    return user


class StaticViewsTests(TestCase):

    def setup(self):
        self.client = Client()

    def test_home_renders_correctly(self):
        """
        Home page should load
        """
        response = self.client.get(reverse("notes:home"))
        self.assertEqual(response.status_code, 200)

    def test_about_renders_correctly(self):
        """
        About page should load
        """
        response = self.client.get(reverse("notes:about"))
        self.assertEqual(response.status_code, 200)

    def test_music_renders_correctly(self):
        """
        Music page should load
        """
        response = self.client.get(reverse("notes:music"))
        self.assertEqual(response.status_code, 200)

    def test_sponsor_renders_correctly(self):
        """
        Sponsor page should load
        """
        response = self.client.get(reverse("notes:sponsor"))
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_renders_correctly(self):
        """
        Privacy Policy page should load
        """
        response = self.client.get(reverse("notes:privacy"))
        self.assertEqual(response.status_code, 200)

    def test_tos_renders_correctly(self):
        """
        Terms of Service page should load
        """
        response = self.client.get(reverse("notes:tos"))
        self.assertEqual(response.status_code, 200)


class NotesListViewTests(TestCase):

    def setup(self):
        self.client = Client()

    def test_list_view_works_correctly(self):
        """
        The view must contain the created notes
        """
        user = create_user(username="TestUser", password="test000")
        self.client.login(username="TestUser", password="test000")
        create_note(title="TestNote1", user=user)
        create_note(title="TestNote2", user=user)
        response = self.client.get(reverse("notes:list"))
        self.assertContains(response, "TestNote1")
        self.assertContains(response, "TestNote2")

    def test_list_view_with_search_works_correctly(self):
        """
        The view must return only the queried notes
        """
        user = create_user(username="TestUser", password="test000")
        self.client.post(reverse("login"), {
            "username": "TestUser",
            "password": "test000"
        })
        create_note(title="TestNote1", user=user)
        create_note(title="TestNote2", user=user)
        response = self.client.get(
            "/notes/?q=TestNote1"
        )  # Did not use reverse. This test will fail if url changes
        self.assertContains(response, "TestNote1")
        self.assertNotContains(response, "TestNote2")


class NotesCreateViewTests(TestCase):

    def setup(self):
        self.client = Client()

    def test_unauthenticated_user_cannot_make_a_note(self):
        """
        Unauthenticated user shouldn't be able to make a note
        """
        self.client.post(
            reverse("notes:create"),
            {
                "title": "Test Note",
                "content": "Test Content",
                "category": "Test cat"
            },
        )
        self.assertEquals(Notes.objects.all().count(), 0)

    def test_authenticated_user_can_make_a_note(self):
        """
        Authenticateded user should be able to succesfully make a note
        """
        create_user(username="TestUser", password="test000")
        self.client.login(username="TestUser", password="test000")
        self.client.post(
            reverse("notes:create"),
            {
                "title": "Test Note",
                "content": "Test Content",
                "category": "Test cat"
            },
        )
        self.assertEquals(Notes.objects.all().count(), 1)


class NotesDeleteViewTests(TestCase):

    def setup(self):
        self.client = Client()

    def test_correct_user_can_delete(self):
        """
        Author of the note should be able to delete the note
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        note = create_note(
            title="TestNote1", user=user1
        )  # User1 created the note and they will try to delete it
        self.client.post(reverse("notes:delete", kwargs={"slug": note.slug}))
        self.assertEquals(Notes.objects.all().count(), 0)

    def test_incorrect_user_cannot_delete(self):
        """
        If user is not author of the note they shouldn't be able to delete the note
        """
        create_user(username="TestUser1", password="test000")
        user2 = create_user(username="TestUser2", password="test000")
        self.client.login(username="TestUser1", password="test000")
        note = create_note(
            title="TestNote1", user=user2
        )  # User2 created the note and user1 will try to delete it
        self.client.post(reverse("notes:delete", kwargs={"slug": note.slug}))
        self.assertEquals(Notes.objects.all().count(), 1)


class NotesDetailsViewTests(TestCase):

    def setup(self):
        self.client = Client()

    def test_correct_user_can_view(self):
        """
        Author of the note should be able to see the note
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        note = create_note(
            title="TestNote1",
            user=user1)  # User1 created the note and they will try to see it
        response = self.client.get(
            reverse("notes:detail", kwargs={"slug": note.slug}))
        self.assertContains(response, "TestNote1")

    def test_incorrect_user_cannot_view(self):
        """
        If user is not author of the note they shouldn't be able to view the note
        """
        create_user(username="TestUser1", password="test000")
        user2 = create_user(username="TestUser2", password="test000")
        self.client.login(username="TestUser1", password="test000")
        note = create_note(
            title="TestNote1",
            user=user2)  # User2 created the note and user1 will try to view it
        response = self.client.get(
            reverse("notes:detail", kwargs={"slug": note.slug}))
        self.assertEquals(response.status_code, 403)


class NotesUpdateViewTests(TestCase):

    def setup(self):
        self.client = Client()

    def test_correct_user_can_update(self):
        """
        Author of the note should be able to succesfully update the note
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        note = create_note(
            title="TestNote1", user=user1
        )  # User1 created the note and they will try to update it
        self.client.post(
            reverse("notes:update", kwargs={"slug": note.slug}),
            {
                "title": "Updated_test_note",
                "content": "test_content",
                "category": "CS"
            },
        )
        self.assertEqual(Notes.objects.all()[0].title, "Updated_test_note")

    def test_incorrect_user_cannot_update(self):
        """
        If user is not author of the note they shouldn't be able to view the note
        """
        create_user(username="TestUser1", password="test000")
        user2 = create_user(username="TestUser2", password="test000")
        self.client.login(username="TestUser1", password="test000")
        note = create_note(
            title="TestNote1", user=user2
        )  # User2 created the note and user1 will try to update it
        self.client.post(
            reverse("notes:update", kwargs={"slug": note.slug}),
            {
                "title": "Updated_test_note",
                "content": "test_content",
                "category": "CS"
            },
        )
        self.assertNotEqual(Notes.objects.all()[0].title, "Updated_test_note")
