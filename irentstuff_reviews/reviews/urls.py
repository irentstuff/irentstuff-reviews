
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root of reviews app maps to index view
    path('list/', views.review_list, name='review_list'),  # URL to list all reviews
    path('<int:review_id>/', views.review_detail, name='review_detail'),  # URL to get details of a specific review
]