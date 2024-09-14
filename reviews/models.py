from django.db import models
from uuid import uuid4

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    rental_id = models.IntegerField(default=1)
    item_id = models.IntegerField(default=1) 
    user_id = models.CharField(max_length=255, default="default_user")
    rating = models.IntegerField(default=5)
    comment = models.TextField(default="Test comment. Happy sunday, funday")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review {self.review_id} - Item {self.item_id}'
