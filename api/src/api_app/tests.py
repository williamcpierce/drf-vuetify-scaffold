from rest_framework import status
from rest_framework.test import APITestCase

from .models import Message


class TestMessageSerializerEndpoint(APITestCase):
    def setUp(self):
        self.url = "/api/message/"
        self.valid_data = {"text": "This is a test message"}
        self.invalid_data = {"text": ""}  # Empty text field

    def test_create_message(self):
        # Test with valid data
        response = self.client.post(self.url, self.valid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().text, self.valid_data["text"])

        # Test with invalid data
        response = self.client.post(self.url, self.invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Message.objects.count(), 1)

    # def test_update_message(self):
    #     # Create a message to update
    #     self.client.post(self.url, self.valid_data, format="json")

    #     # Test with valid data
    #     new_data = self.valid_data.copy()
    #     new_data["text"] = "This is an updated message"
    #     response = self.client.put(f"{self.url}1/", new_data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Message.objects.count(), 1)
    #     self.assertEqual(Message.objects.get().text, new_data["text"])

    #     # Test with invalid data
    #     response = self.client.put(f"{self.url}1/", self.invalid_data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(Message.objects.count(), 1)
    #     self.assertEqual(Message.objects.get().text, new_data["text"])
