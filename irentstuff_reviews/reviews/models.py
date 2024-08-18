from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    item_id = models.IntegerField()  # ForeignKey can be added once the Item model is in a separate app
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review {self.id} for Item {self.item_id}'

class Item(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title