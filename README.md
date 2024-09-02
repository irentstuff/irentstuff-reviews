# iRentStuff Reviews Microservice 

This project is a microservice for managing reviews in the iRentStuff application. It is built using Django and Django REST Framework.

## Table of Contents

## Table of Contents
- [iRentStuff Reviews Microservice](#irentstuff-reviews-microservice)
  - [Table of Contents](#table-of-contents)
  - [Table of Contents](#table-of-contents-1)
  - [Installation](#installation)
  - [Run the Project Locally](#run-the-project-locally)
  - [API Endpoints](#api-endpoints)
  - [Testing the APIs with Postman](#testing-the-apis-with-postman)
  - [Authentication with JWT](#authentication-with-jwt)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/irentstuff/irentstuff-reviews.git
   cd irentstuff-reviews
1. Set up virtual env: 
   ``` bash 
   python -m venv venv
   source venv/bin/activate
1. Install the dependencies:
   ``` bash
   pip install -r requirements.txt

## Run the Project Locally

1. The project will be running on http://127.0.0.1:8000/.
    
    ``` bash
    python manage.py migrate
    python manage.py runserver

## API Endpoints
Below are the main API endpoints you can test:

1. Create a Review: POST /api/v1/reviews/
1. Get Reviews for an Item: GET /api/v1/items/<uuid:item_id>/reviews/
1. Get a Review by ID: GET /api/v1/reviews/<uuid:review_id>/
1. Update a Review: PUT /api/v1/reviews/<uuid:review_id>/
1. Delete a Review: DELETE /api/v1/reviews/<uuid:review_id>/
1. Get Reviews for a User: GET /api/v1/users/<uuid:user_id>/reviews/
1. Get Item Rating: GET /api/v1/items/<uuid:item_id>/rating/

## Testing the APIs with Postman

1. Create a Review (POST)
- URL: http://127.0.0.1:8000/api/v1/reviews/
- Method: POST
- Request Body (JSON): 
  ``` json
  {
  "rental_id": "4be6ed3c-08da-418b-ac4f-eeefd7ad16c5",
  "item_id": "3beed80b-69a2-42f0-b276-8e8684bc9076",
  "user_id": "79f08fe1-0074-4520-af15-57eb12f3865d",
  "rating": 5,
  "comment": "Great product!"
    }

2. Get Reviews for an Item (GET)
- URL: http://127.0.0.1:8000/api/v1/items/<item_id>/reviews/
- Method: GET
- Replace `<item_id>` with the actual UUID of the item.

3. Get a Review by ID (GET)
- URL: http://127.0.0.1:8000/api/v1/reviews/<review_id>/
- Method: GET
- Replace `<review_id>` with the actual UUID of the review.

4. Update a Review (PUT)
- URL: http://127.0.0.1:8000/api/v1/reviews/<review_id>/
- Method: PUT
- Request Body (JSON): 
  ``` json
  {
  "rating": 4,
  "comment": "Updated comment"
    }
- Replace `<review_id>` with the actual UUID of the review.
- Headers:
    Authorization: Bearer `<your-jwt-access-token>` - refer to [Authentication with JWT](#authentication-with-jwt)

5. Delete a Review (DELETE)
- URL: http://127.0.0.1:8000/api/v1/reviews/<review_id>/
- Method: DELETE
- Replace `<review_id>` with the actual UUID of the review.
- Headers:
    Authorization: Bearer `<your-jwt-access-token>` - refer to [Authentication with JWT](#authentication-with-jwt)


6. Get Reviews for a User (GET)
- URL: http://127.0.0.1:8000/api/v1/users/<user_id>/reviews/
- Method: GET
- Replace `<user_id>` with the actual UUID of the user.

7. Get Item Rating (GET)
- URL: http://127.0.0.1:8000/api/v1/items/<item_id>/rating/
- Method: GET
- Replace `<item_id>` with the actual UUID of the item.

## Authentication with JWT
For certain requests, such as updating and deleting reviews, you will need to provide an authentication token.

1. Generate a JWT Token (POST)
- URL: http://127.0.0.1:8000/api/token/
- Method: POST
- Body: JSON
  ```json
  {
  "username": "your-username",
  "password": "your-password"
    }
- Response: JSON
  ``` json 
  {
  "access": "your-access-token",
  "refresh": "your-refresh-token"
    }
2. Using the JWT Token in Postman
Once you get the access token from the above API, you need to include it in the Authorization header of your PUT and DELETE requests.

    In Postman, for the PUT and DELETE requests:
    - Go to the Authorization tab.
    - Select Bearer Token from the dropdown.
    - Paste your JWT access token in the Token field.
