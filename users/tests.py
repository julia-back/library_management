from rest_framework.test import APITestCase
from django.shortcuts import reverse
from .models import User
from rest_framework import status
from django.contrib.auth.models import Group


class TokenTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", username="test", password="1234")

    def test_token_obtain_pair_and_refresh(self):
        url = reverse("users:token_pair")
        user_data = {
            "email": self.user.email,
            "username": self.user.username,
            "password": "1234",
        }

        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
        self.assertTrue(response.json().get("access"))
        self.assertTrue(response.json().get("refresh"))

        refresh = response.json().get("refresh")

        url = reverse("users:token_refresh")
        refresh_data = {
            "refresh": refresh
        }

        response = self.client.post(url, refresh_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json().get("access"))


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", username="test", password="1234")

        self.user_admin = User.objects.create_user(email="test_admin@test.com", username="test_admin", password="1234")
        self.admin_group = Group.objects.create(name="admin")
        self.user_admin.groups.add(self.admin_group)

    def test_create_user(self):
        url = reverse("users:user_create")
        user_data = {
            "email": "test_2@test.com",
            "username": "test_2",
            "password": "1234",
        }

        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.json()), 3)

    def test_list_user(self):
        url = reverse("users:user_list")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_retrieve_user(self):
        url = reverse("users:user_retrieve", args=[self.user.pk])
        self.user_2 = User.objects.create_user(email="test_2@test.com", username="test_2", password="1234")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user_2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_put(self):
        url = reverse("users:user_update", args=[self.user.pk])
        self.user_2 = User.objects.create_user(email="test_2@test.com", username="test_2", password="1234")
        user_data = {
            "email": "test@test.com",
            "username": "test_update",
            "password": "1234",
        }

        response = self.client.put(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user_2)
        response = self.client.put(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.put(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("username"), "test_update")

    def test_update_user_patch(self):
        url = reverse("users:user_update", args=[self.user.pk])
        self.user_2 = User.objects.create_user(email="test_2@test.com", username="test_2", password="1234")
        user_data = {
            "username": "test_update",
        }

        response = self.client.patch(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user_2)
        response = self.client.patch(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.patch(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("username"), "test_update")

    def test_destroy_user(self):
        url = reverse("users:user_destroy", args=[self.user.pk])
        self.user_2 = User.objects.create_user(email="test_2@test.com", username="test_2", password="1234")

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user_2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user_admin)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
