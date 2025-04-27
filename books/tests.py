from rest_framework.test import APITestCase
from django.shortcuts import reverse
from .models import Book, Author
from users.models import User
from django.contrib.auth.models import Group
from rest_framework import status


class BookTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", username="test", password="1234")

        self.user_admin = User.objects.create_user(email="test_admin@test.com", username="test_admin", password="1234")
        self.admin_group = Group.objects.create(name="admin")
        self.user_admin.groups.add(self.admin_group)

        self.author = Author.objects.create(first_name="Author_1", last_name="Author_1")
        self.book = Book.objects.create(name="book_1", description="description_1",
                                        genre="genre_1", language="ru")
        self.book.author.add(self.author)

    def test_create_book(self):
        url = reverse("books:book_create")
        book_data = {
            "name": "book_2",
            "description": "description_2",
            "genre": "genre_2",
            "language": "eng",
            "author": self.author.pk
        }

        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.post(url, book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.json()), 11)

    def test_list_book(self):
        url = reverse("books:book_list")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve_book(self):
        url = reverse("books:book_retrieve", args=[self.book.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 11)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 11)

    def test_update_book_put(self):
        url = reverse("books:book_update", args=[self.book.pk])
        book_data_put = {
            "name": "book_2_put",
            "description": "description_2",
            "genre": "genre_2",
            "language": "eng",
            "author": self.author.pk
        }

        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.put(url, book_data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 11)
        self.assertEqual(response.json().get("name"), book_data_put.get("name"))

    def test_update_book_patch(self):
        url = reverse("books:book_update", args=[self.book.pk])
        book_data_patch = {
            "name": "book_2_patch",
        }

        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.patch(url, book_data_patch)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 11)
        self.assertEqual(response.json().get("name"), book_data_patch.get("name"))

    def test_destroy_book(self):
        url = reverse("books:book_destroy", args=[self.book.pk])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AuthorTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", username="test", password="1234")

        self.user_admin = User.objects.create_user(email="test_admin@test.com", username="test_admin", password="1234")
        self.admin_group = Group.objects.create(name="admin")
        self.user_admin.groups.add(self.admin_group)

        self.author = Author.objects.create(first_name="Author_1", last_name="Author_1")

    def test_create_author(self):
        url = reverse("books:author_create")
        author_data = {
            "first_name": "Author_2",
            "last_name": "Author_2",
        }

        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, author_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.post(url, author_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.json()), 5)

    def test_list_author(self):
        url = reverse("books:author_list")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve_author(self):
        url = reverse("books:author_retrieve", args=[self.author.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.get(url)
        self.assertEqual(len(response.json()), 5)

    def test_update_author_put(self):
        url = reverse("books:author_update", args=[self.author.pk])
        author_data_put = {
            "first_name": "Author_2_put",
            "last_name": "Author_2_put",
        }

        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.put(url, author_data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)
        self.assertEqual(response.json().get("first_name"), author_data_put.get("first_name"))

    def test_update_author_patch(self):
        url = reverse("books:author_update", args=[self.author.pk])
        author_data_patch = {
            "first_name": "Author_2_patch",
        }

        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.patch(url, author_data_patch)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)
        self.assertEqual(response.json().get("first_name"), author_data_patch.get("first_name"))

    def test_destroy_author(self):
        url = reverse("books:author_destroy", args=[self.author.pk])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
