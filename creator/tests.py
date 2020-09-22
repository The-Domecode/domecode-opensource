from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Product
from django.contrib.auth.models import User

# Create your tests here.


def create_product(name, user):
    product = Product(name=name, user=user)
    product.save()
    return product


def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    user.save()
    return user


class ProductListViewTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_list_view_works_correctly(self):
        """
        The view must contain the creator's products
        """
        user = create_user(username="TestUser", password="test000")
        self.client.login(username="TestUser", password="test000")
        create_product(name="TestProduct1", user=user)
        create_product(name="TestProduct2", user=user)
        response = self.client.get(reverse("creator:list"))
        self.assertContains(response, "TestProduct1")
        self.assertContains(response, "TestProduct2")

    def test_creator_can_see_only_their_product(self):
        """
        A creator can only see their product
        """
        user1 = create_user(username="TestUser1", password="test000")
        user2 = create_user(username="TestUser2", password="test000")

        self.client.login(username="TestUser1", password="test000")
        create_product(name="TestProduct1", user=user1)
        create_product(name="TestProduct2", user=user2)
        response = self.client.get(reverse("creator:list"))
        self.assertContains(response, "TestProduct1")
        self.assertNotContains(response, "TestProduct2")

    def test_list_view_unauth_user_gets_redirected(self):
        """
        The view must redirect unauthenticated users
        """
        user = create_user(username="TestUser", password="test000")
        create_product(name="TestProduct1", user=user)
        response = self.client.get(reverse("creator:list"))
        self.assertNotEquals(response.status_code, 200)


class ProductCreateViewTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_unauthenticated_user_cannot_make_a_product(self):
        """
        Unauthenticated user shouldn't be able to make a product
        """
        self.client.post(
            reverse("creator:create"),
            {
                "name": "Test Product",
                "description": "Test",
                "category": "Test cat",
                "contributors": "None",
            },
        )
        self.assertEquals(Product.objects.all().count(), 0)

    def test_authenticated_user_can_make_a_product(self):
        """
        Authenticateded user should be able to succesfully make a product
        """
        create_user(username="TestUser", password="test000")
        self.client.login(username="TestUser", password="test000")
        self.client.post(
            reverse("creator:create"),
            {
                "name": "Test Product",
                "description": "Test",
                "category": "Test cat",
                "contributors": "None",
            },
        )
        self.assertEquals(Product.objects.all().count(), 1)


class ProductDeleteViewTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_correct_user_can_delete(self):
        """
        Author of the product should be able to delete the product
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        product = create_product(name="TestProduct1", user=user1)
        # User1 created the product and they will try to delete it
        self.client.post(reverse("creator:delete", kwargs={"slug": product.slug}))
        self.assertEquals(Product.objects.all().count(), 0)

    def test_incorrect_user_cannot_delete(self):
        """
        If user is not author of the product they shouldn't be able to delete the product
        """
        create_user(username="TestUser1", password="test000")
        user2 = create_user(username="TestUser2", password="test000")
        self.client.login(username="TestUser1", password="test000")
        product = create_product(name="TestProduct1", user=user2)
        # User2 created the product and user1 will try to delete it
        self.client.post(reverse("creator:delete", kwargs={"slug": product.slug}))
        self.assertEquals(Product.objects.all().count(), 1)


class ProductDetailsViewTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_correct_user_can_view(self):
        """
        Author of the product should be able to see the Product
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        product = create_product(name="TestProduct1", user=user1)
        # User1 created the product and they will try to see it
        response = self.client.get(
            reverse("creator:detail", kwargs={"slug": product.slug})
        )
        self.assertContains(response, "TestProduct1")

    def test_incorrect_user_can_also_view(self):
        """
        If user is not author of the product they should also be able to view the product
        """
        create_user(username="TestUser1", password="test000")
        user2 = create_user(username="TestUser2", password="test000")
        self.client.login(username="TestUser1", password="test000")
        product = create_product(name="TestProduct1", user=user2)
        # User2 created the product and user1 will try to view it
        response = self.client.get(
            reverse("creator:detail", kwargs={"slug": product.slug})
        )
        self.assertContains(response, "TestProduct1")
        self.client.logout()
        response = self.client.get(
            reverse("creator:detail", kwargs={"slug": product.slug})
        )
        self.assertContains(response, "TestProduct1")


class ProductUpdateViewTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_correct_user_can_update(self):
        """
        Creator of the product should be able to succesfully update the product
        """
        user1 = create_user(username="TestUser1", password="test000")
        self.client.login(username="TestUser1", password="test000")
        product = create_product(name="TestProduct1", user=user1)
        # User1 created the product and they will try to update it
        self.client.post(
            reverse("creator:update", kwargs={"slug": product.slug}),
            {
                "name": "Updated_test_product",
                "description": "test_description",
                "category": "CS",
                "contributors": "None",
            },
        )
        self.assertEqual(Product.objects.all()[0].name, "Updated_test_product")

    def test_incorrect_user_cannot_update(self):
        """
        If user is not author of the product they shouldn't be able to update the product
        """
        create_user(username="TestUser1", password="test000")
        user2 = create_user(username="TestUser2", password="test000")
        self.client.login(username="TestUser1", password="test000")
        product = create_product(name="TestProduct1", user=user2)
        # User2 created the product and user1 will try to update it
        self.client.post(
            reverse("creator:update", kwargs={"slug": product.slug}),
            {
                "name": "Updated_test_product",
                "description": "test_description",
                "category": "CS",
                "contributors": "None",
            },
        )
        self.assertNotEqual(Product.objects.all()[0].name, "Updated_test_product")
