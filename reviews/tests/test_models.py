from django.test import TestCase
from reviews.models import Review
from django.utils import timezone
from uuid import UUID
from django.core.exceptions import ValidationError


class ReviewModelTest(TestCase):
    def setUp(self):
        self.review = Review.objects.create(
            rental_id=1,
            item_id=1,
            user_id="test_user",
            rating=4,
            comment="Test comment",
        )

    def test_review_creation(self):
        self.assertTrue(isinstance(self.review, Review))
        self.assertIsInstance(self.review.review_id, UUID)
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, "Test comment")

    def test_auto_timestamps(self):
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)
        self.assertLessEqual(self.review.created_at, timezone.now())
        self.assertLessEqual(self.review.updated_at, timezone.now())

    def test_string_representation(self):
        self.assertEqual(
            str(self.review),
            f"Review {self.review.review_id} - Item {self.review.item_id}",
        )


# additional tests to write
# Invalid Rating: Test that a ValidationError is raised if the rating is not between 1 and 5.
# Invalid Comment Length: Test that a ValidationError is raised if the comment exceeds 1000 characters.
# Timestamp Accuracy - Ensure that created_at and updated_at are set correctly, and updated_at changes when the model is updated.
# UUID Field - Ensure that the review_id is properly generated as a UUID.
