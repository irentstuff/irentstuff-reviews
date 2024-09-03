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

def index(request):
    return HttpResponse("Hello, this is the irentstuff-reviews page.")

class CreateReview(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class GetReviewsForItem(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        return Review.objects.filter(item_id=item_id)

class GetReviewById(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'review_id'

class UpdateReview(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'review_id'

    def put(self, request, *args, **kwargs):
        print("PUT request received")  # Debugging line
        return super().put(request, *args, **kwargs)

class DeleteReview(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'review_id'

class GetReviewsForUser(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Review.objects.filter(user_id=user_id)

# Mocked item data version
class GetItemRating(generics.RetrieveAPIView):
    serializer_class = ReviewSerializer

    @patch('requests.get')
    def get(self, request, mock_get, *args, **kwargs):
        item_id = self.kwargs['item_id']

        # Define mock data for multiple items
        mock_items_data = {
            '77d98bfe-9e24-4252-9084-064a953afc22': {
                'id': '77d98bfe-9e24-4252-9084-064a953afc22',
                'name': 'Mocked Item Name 1',
                'description': 'This is a mocked description of item 1.'
            },
            '3beed80b-69a2-42f0-b276-8e8684bc9076': {
                'id': '3beed80b-69a2-42f0-b276-8e8684bc9076',
                'name': 'Mocked Item Name 2',
                'description': 'This is a mocked description of item 2.'
            },
            'f3a983a5-5d3c-4b0e-8e2d-1b0b9ffbc16e': {
                'id': 'f3a983a5-5d3c-4b0e-8e2d-1b0b9ffbc16e',
                'name': 'Mocked Item Name 3',
                'description': 'This is a mocked description of item 3.'
            },
            'a67c7c48-7b5c-4b42-9834-cf5a1dc4975b': {
                'id': 'a67c7c48-7b5c-4b42-9834-cf5a1dc4975b',
                'name': 'Mocked Item Name 4',
                'description': 'This is a mocked description of item 4.'
            }
            # Add more items here if needed
        }

        # Fetch the relevant item data based on item_id
        item_data = mock_items_data.get(item_id)
        if not item_data:
            raise Http404(f'Item with id {item_id} not found.')

        # Fetch reviews for the item in the reviews database
        reviews = Review.objects.filter(item_id=item_id)
        total_reviews = reviews.count()
        if total_reviews == 0:
            return Response({"item_id": item_id, "average_rating": None, "total_reviews": 0})

        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        return Response({
            "item_id": item_id,
            "item_name": item_data.get('name'),  # Using mocked item data
            "average_rating": average_rating,
            "total_reviews": total_reviews
        })

class YourProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view"})
