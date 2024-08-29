from rest_framework import generics
from rest_framework.response import Response  
from .models import Review
from .serializers import ReviewSerializer
from django.db.models import Avg
from unittest.mock import patch
import requests
from django.http import Http404
from django.http import HttpResponse


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

        # Define the mock response data
        mock_item_data = {
            'id': item_id,
            'name': 'Mocked Item Name',
            'description': 'This is a mocked description of the item.'
        }

        # Configure the mock to return the mock data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_item_data

        # Simulate the API call (which will now use the mocked response)
        try:
            response = requests.get(f'http://mocked-item-service-url/items/{item_id}/')
            response.raise_for_status()
            item_data = response.json()
        except requests.exceptions.RequestException as e:
            raise Http404(f'Item with id {item_id} not found. {e}')

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
