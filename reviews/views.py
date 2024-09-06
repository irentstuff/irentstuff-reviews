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
        item_id = self.kwargs['item_id']
        return Review.objects.filter(item_id=item_id)

class GetReviewById(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'review_id'
    permission_classes = [AllowAny]

class UpdateReview(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'review_id'
    permission_classes = [AllowAny]

    def put(self, request, *args, **kwargs):
        print("PUT request received")  # Debugging line
        return super().put(request, *args, **kwargs)

class DeleteReview(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'review_id'
    permission_classes = [AllowAny]

class GetReviewsForUser(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Review.objects.filter(user_id=user_id)

# Mocked item data version
class GetItemRating(generics.RetrieveAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['item_id']
        print(f"Received item_id in URL: {item_id}")

        # Fetch reviews for the given item_id
        reviews = Review.objects.filter(item_id=item_id)
        if not reviews.exists():
            print(f"No reviews found for item_id: {item_id}")
            raise Http404(f'Item with id {item_id} not found in reviews.')
        
        total_reviews = reviews.count()
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        print(f"Total reviews: {total_reviews}, Average rating: {average_rating}")

        return Response({
            "item_id": item_id,
            "average_rating": average_rating,
            "total_reviews": total_reviews
        })

class YourProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view"})
