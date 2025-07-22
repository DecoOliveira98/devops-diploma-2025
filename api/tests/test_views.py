from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book

class BookViewTest(APITestCase):
    
    def setUp(self):
        self.book = Book.objects.create(
            title="Demo Book",
            description="Test description",
            author="Author Name",
            isbn="1234567890123",
            published_date="2025-07-22"
        )

    def test_list_books(self):
       
        url = reverse('api:books-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        body = response.json()
        self.assertGreaterEqual(len(body), 1)
        self.assertEqual(body[0]["title"], self.book.title)

    def test_create_book(self):
        url = reverse('api:books-list')
        data = {
            "title": "New Book",
            "description": "Created by test",
            "author": "Tester",
            "isbn": "9876543210987",
            "published_date": "2025-07-23"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_delete_book(self):
        url = reverse('api:books-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())


class HealthViewTest(APITestCase):
    def test_health_endpoint(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["status"], "ok")
