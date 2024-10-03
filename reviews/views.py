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

from .metrics import (
    create_review_counter, 
    create_review_latency, 
    get_reviews_latency,
    update_review_latency,
    delete_review_latency,
    increment_error_count,
    increment_successful_request_count,
    increment_reviews_fetched,
    increment_unauthorized_access
)

import time

def index(request):
    return HttpResponse("Hello, this is the irentstuff-reviews page.")

class CreateReview(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        start_time = time.time()
        user_id = request.data.get('user_id')
        item_id = request.data.get('item_id')

        request_counter.inc()

        if not user_id or not item_id:
            return Response({"error": "user_id and item_id are required"}, status=400)

        # Increment counter with labels
        create_review_counter.labels(user_id=user_id, item_id=item_id).inc()

        # Create the review
        response = super().post(request, *args, **kwargs)

        # Track errors if response has status code >= 400
        if response.status_code >= 400:
            increment_error_count(response.status_code)

        # Track successful review creation
        if response.status_code == 201:  # Successful creation
            increment_successful_request_count()

        # Record request latency
        latency = time.time() - start_time
        create_review_latency.observe(latency)

        return response

    
class GetReviewsForItem(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        item_id = self.kwargs["item_id"]
        return Review.objects.filter(item_id=item_id)

    def list(self, request, *args, **kwargs):
        start_time = time.time()
        queryset = self.get_queryset()
        item_id = self.kwargs["item_id"]

        request_counter.inc()

        if not queryset.exists():
            increment_error_count(404)
            return Response({"message": "No reviews for this item found."}, status=404)

        increment_reviews_fetched(item_id=item_id, count=queryset.count())

        # Record request latency
        latency = time.time() - start_time
        record_request_latency(latency)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class GetReviewById(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "review_id"
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        review_id = kwargs["review_id"]

        # Increment total request counter
        request_counter.inc()

        try:
            review = Review.objects.get(review_id=review_id)
        except Review.DoesNotExist:
            increment_error_count(404) 
            return Response({"message": "No such review found."}, status=404)
        return Response(self.get_serializer(review).data)

class UpdateReview(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "review_id"
    permission_classes = [AllowAny]

    def put(self, request, *args, **kwargs):
        start_time = time.time()
        review_id = kwargs.get("review_id")
        try:
            # Check if the review exists
            review = Review.objects.get(review_id=review_id)
        except Review.DoesNotExist:
            increment_error_count(404)
            return Response({"message": "No such review found."}, status=404)

        response = super().put(request, *args, **kwargs)

        if response.status_code == 200:  # Successful update
            increment_successful_request_count()

        # Record latency
        latency = time.time() - start_time
        update_review_latency.observe(latency)


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
        start_time = time.time()
        review_id = kwargs.get("review_id")
        try:
            # Check if the review exists
            review = Review.objects.get(review_id=review_id)
        except Review.DoesNotExist:
            increment_error_count(404) 
            return Response({"message": "No such review found."}, status=404)

        response = super().delete(request, *args, **kwargs)

        # Record latency
        latency = time.time() - start_time
        delete_review_latency.observe(latency)

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
            increment_error_count(404) 
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
            increment_error_count(404) 
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
