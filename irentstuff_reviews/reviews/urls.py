from django.urls import path
from .views import CreateReview, GetReviewsForItem, GetReviewById, UpdateReview, DeleteReview, GetReviewsForUser, GetItemRating

urlpatterns = [
    path('reviews/', CreateReview.as_view(), name='create-review'),
    path('items/<uuid:item_id>/reviews/', GetReviewsForItem.as_view(), name='get-reviews-for-item'),
    path('reviews/<uuid:review_id>/', GetReviewById.as_view(), name='get-review-by-id'),
    path('reviews/<uuid:review_id>/', UpdateReview.as_view(), name='update-review'),
    path('reviews/<uuid:review_id>/', DeleteReview.as_view(), name='delete-review'),
    path('users/<uuid:user_id>/reviews/', GetReviewsForUser.as_view(), name='get-reviews-for-user'),
    path('items/<uuid:item_id>/rating/', GetItemRating.as_view(), name='get-item-rating'),
]
