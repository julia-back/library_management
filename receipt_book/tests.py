from rest_framework.test import APITestCase
from django.shortcuts import reverse
from .models import ReceiptBook
from users.models import User
from django.contrib.auth.models import Group
from rest_framework import status
from books.models import Book, Author
from datetime import date


class ReceiptBookTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", username="test", password="1234")
        self.user_owner = User.objects.create_user(email="test_owner@test.com", username="test_owner", password="1234")

        self.user_admin = User.objects.create_user(email="admin@admin.com", username="admin", password="1234")
        self.group_admin = Group.objects.create(name="admin")
        self.user_admin.groups.add(self.group_admin)

        self.author = Author.objects.create(first_name="Author_1", last_name="Author_1")
        self.book = Book.objects.create(name="book_1", description="description_1",
                                        genre="genre_1", language="ru")
        self.book.author.add(self.author)

        self.receipt = ReceiptBook.objects.create(user=self.user_owner, book=self.book)

    def test_create_receipt_book(self):
        url = reverse("receipt:receipt_create")
        receipt_data = {
            "user": self.user_owner.pk,
            "book": self.book.pk,
        }

        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.post(url, receipt_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.json()), 6)

        response = self.client.post(url, receipt_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json().get("non_field_errors"), ["Книга уже на руках."])

    def test_destroy_receipt(self):
        url = reverse("receipt:receipt_destroy", args=[self.receipt.pk])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_receipt(self):
        url = reverse("receipt:receipt_list")
        self.receipt_2 = ReceiptBook.objects.create(user=self.user, book=self.book)
        self.receipt_3 = ReceiptBook.objects.create(user=self.user_owner, book=self.book)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

        self.client.force_authenticate(user=self.user_owner)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)

    def test_retrieve_receipt(self):
        url = reverse("receipt:receipt_retrieve", args=[self.receipt.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get("detail"), "You do not have permission to perform this action.")

        self.client.force_authenticate(user=self.user_owner)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 6)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 6)

    def test_return_book(self):
        url = reverse("receipt:return_book", args=[self.receipt.pk])

        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_owner)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 6)
        self.assertEqual(response.json().get("return_date"), date.today().strftime("%Y-%m-%d"))
