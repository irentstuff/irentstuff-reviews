from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Review

def index(request):
    return HttpResponse("Welcome to the iRentStuff Reviews Service")

def review_list(request):
    reviews = Review.objects.all().values()
    return JsonResponse(list(reviews), safe=False)

def review_detail(request, review_id):
    review = Review.objects.filter(id=review_id).values().first()
    return JsonResponse(review, safe=False)


# def review_list(request):
#     reviews = Review.objects.all().values()
#     # Return test data
#     test_data = [
#         {
#             "id": 1234,
#             "author_id": 10,
#             "rental_id": 1,
#             "rating": 5,
#             "comment": "Test comment for review list. Cool beans",
#             "created_date": "2024-08-17T12:00:00Z"
#         }
#     ]
#     return JsonResponse(test_data, safe=False)

# def review_detail(request, review_id):
#     # Return test data
#     test_data = {
#         "id": review_id,
#         "author_id": 1,
#         "rental_id": 1,
#         "rating": 4,
#         "comment": "Test comment for review detail",
#         "created_date": "2024-08-17T12:00:00Z"
#     }
#     return JsonResponse(test_data)