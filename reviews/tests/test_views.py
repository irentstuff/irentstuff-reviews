# from django.urls import reverse
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APIClient
# from reviews.models import Review
# from django.contrib.auth.models import User
# from uuid import uuid4


# class ReviewViewsTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username="testuser", password="testpass")
#         self.review = Review.objects.create(
#             rental_id=1,
#             item_id=1,
#             user_id=self.user.id,
#             rating=5,
#             comment="Test review",
#         )

#     def test_create_review(self):
#         response = self.client.post(
#             reverse("create-review"),
#             {
#                 "rental_id": 1,
#                 "item_id": 1,
#                 "user_id": "test_user",
#                 "rating": 5,
#                 "comment": "A new review comment",
#             },
#             format="json",
#         )

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Review.objects.count(), 2)


# # # additional tests to write
# # Invalid Rating in POST: Test that trying to create a review with an invalid rating returns a 400 Bad Request.
# # Invalid Comment Length in POST: Test that a review with too long of a comment returns 400 Bad Request.
# # Valid Update: Test that a review can be updated with valid data.
# # Invalid Update: Test that trying to update a review with invalid data returns the correct error.

# # Test that a review can be successfully deleted.
# # Test trying to delete a non-existent review returns 404 Not Found.

# # No Reviews Found: Test that trying to retrieve reviews for an item or user with no reviews returns a 404 Not Found.
# # Fetching Reviews for an Item: Test fetching reviews for an existing item.

# # Get Average Rating: Test the correct average rating and total number of reviews for an item.
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from reviews.models import Review
from django.contrib.auth.models import User


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
                "user_id": self.user.id,
                "rating": 5,
                "comment": "A new review comment",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)

    def test_invalid_rating_in_post(self):
        # Invalid rating (e.g., rating should be between 1-5)
        response = self.client.post(
            reverse("create-review"),
            {
                "rental_id": 1,
                "item_id": 1,
                "user_id": self.user.id,
                "rating": 10,  # Invalid rating
                "comment": "Invalid rating test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_comment_length_in_post(self):
        # Invalid comment length (e.g., too long)
        long_comment = "A" * 1001  # Assuming max length is 1000 characters
        response = self.client.post(
            reverse("create-review"),
            {
                "rental_id": 1,
                "item_id": 1,
                "user_id": self.user.id,
                "rating": 5,
                "comment": long_comment,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_review(self):
        # Valid update
        response = self.client.put(
            reverse("update-review", kwargs={"review_id": self.review.review_id}),
            {
                "rental_id": 1,
                "item_id": 1,
                "user_id": self.user.id,
                "rating": 4,
                "comment": "Updated comment",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.review.refresh_from_db()
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, "Updated comment")

    def test_invalid_update_review(self):
        # Invalid update with wrong data
        response = self.client.put(
            reverse("update-review", kwargs={"review_id": self.review.review_id}),
            {
                "rental_id": 1,
                "item_id": 1,
                "user_id": self.user.id,
                "rating": 10,  # Invalid rating
                "comment": "Updated comment",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_review(self):
        # Delete review successfully
        response = self.client.delete(
            reverse("delete-review", kwargs={"review_id": self.review.review_id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.count(), 0)

    def test_delete_non_existent_review(self):
        # Try to delete a non-existent review
        response = self.client.delete(
            reverse("delete-review", kwargs={"review_id": 999}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_no_reviews_found_for_item(self):
        # Test no reviews found for an item
        response = self.client.get(reverse("get-reviews-item", kwargs={"item_id": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_fetching_reviews_for_item(self):
        # Fetching reviews for an existing item
        response = self.client.get(reverse("get-reviews-item", kwargs={"item_id": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_average_rating(self):
        # Get average rating and total reviews
        Review.objects.create(
            rental_id=1, item_id=1, user_id=self.user.id, rating=3, comment="Another review"
        )
        response = self.client.get(reverse("get-item-rating", kwargs={"item_id": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["average_rating"], 4.0)
        self.assertEqual(response.data["total_reviews"], 2)
