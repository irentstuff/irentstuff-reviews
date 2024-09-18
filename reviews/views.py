from rest_framework import generics
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from django.db.models import Avg
from unittest.mock import patch
import requests
from django.http import Http404, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


def index(request):
    return HttpResponse("Hello, this is the irentstuff-reviews page.")


class CreateReview(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]


class GetReviewsForItem(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        item_id = self.kwargs["item_id"]
        return Review.objects.filter(item_id=item_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "No reviews for this item found."}, status=404)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GetReviewById(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "review_id"
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        review_id = kwargs["review_id"]
        try:
            review = Review.objects.get(review_id=review_id)
        except Review.DoesNotExist:
            return Response({"message": "No such review found."}, status=404)
        return Response(self.get_serializer(review).data)


class UpdateReview(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "review_id"
    permission_classes = [AllowAny]

    def put(self, request, *args, **kwargs):
        review_id = kwargs.get("review_id")
        try:
            # Check if the review exists
            review = Review.objects.get(review_id=review_id)
        except Review.DoesNotExist:
            return Response({"message": "No such review found."}, status=404)

        response = super().put(request, *args, **kwargs)
        return Response(
            {
                "message": "Review updated successfully.",
                "review_id": review_id,
                "data": response.data,
            },
            status=200,
        )


class DeleteReview(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "review_id"
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        review_id = kwargs.get("review_id")
        try:
            # Check if the review exists
            review = Review.objects.get(review_id=review_id)
        except Review.DoesNotExist:
            return Response({"message": "No such review found."}, status=404)

        super().delete(request, *args, **kwargs)
        return Response(
            {"message": "Review deleted successfully.", "review_id": review_id},
            status=200,
        )


class GetReviewsForUser(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        queryset = Review.objects.filter(user_id=user_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "No reviews found for this user."}, status=404)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Mocked item data version
class GetItemRating(generics.RetrieveAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        item_id = self.kwargs["item_id"]
        print(f"Received item_id in URL: {item_id}")

        # Fetch reviews for the given item_id
        reviews = Review.objects.filter(item_id=item_id)
        if not reviews.exists():
            return Response(
                {
                    "message": f"No such item rating found.",
                    "average_rating": None,
                    "total_reviews": 0,
                },
                status=404,
            )

        total_reviews = reviews.count()
        average_rating = reviews.aggregate(Avg("rating"))["rating__avg"]
        print(f"Total reviews: {total_reviews}, Average rating: {average_rating}")

        return Response(
            {
                "item_id": item_id,
                "average_rating": average_rating,
                "total_reviews": total_reviews,
            }
        )


class YourProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view"})
