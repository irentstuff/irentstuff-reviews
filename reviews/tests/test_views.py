from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from reviews.models import Review
from django.contrib.auth.models import User
from uuid import uuid4


class ReviewViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.review = Review.objects.create(
            rental_id=1,
            item_id=1,
            user_id=self.user.id,
            rating=5,
            comment="Test review",
        )

    def test_create_review(self):
        response = self.client.post(
            reverse("create-review"),
            {
                "rental_id": 1,
                "item_id": 1,
                "user_id": "test_user",
                "rating": 5,
                "comment": "A new review comment",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)


# # additional tests to write
# Invalid Rating in POST: Test that trying to create a review with an invalid rating returns a 400 Bad Request.
# Invalid Comment Length in POST: Test that a review with too long of a comment returns 400 Bad Request.
# Valid Update: Test that a review can be updated with valid data.
# Invalid Update: Test that trying to update a review with invalid data returns the correct error.

# Test that a review can be successfully deleted.
# Test trying to delete a non-existent review returns 404 Not Found.

# No Reviews Found: Test that trying to retrieve reviews for an item or user with no reviews returns a 404 Not Found.
# Fetching Reviews for an Item: Test fetching reviews for an existing item.

# Get Average Rating: Test the correct average rating and total number of reviews for an item.
