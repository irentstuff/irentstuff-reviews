from django.contrib import admin

from django.contrib import admin
from .models import Review

# admin.site.register(Review)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "review_id",
        "item_id",
        "user_id",
        "rating",
        "comment",
        "created_at",
    )
    search_fields = ("item_id", "user_id", "comment")
