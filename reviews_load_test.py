from locust import HttpUser, task, between

class ReviewsUser(HttpUser):
    # Simulate a wait time between user tasks (to mimic real users)
    wait_time = between(1, 3)

    # Test creating a new review
    @task(1)
    def create_review(self):
        review_data = {
            "item_id": 1,
            "user_id": "shermin",
            "rating": 4,
            "comment": "Great item! Highly recommend!"
        }
        self.client.post("/reviews/", json=review_data)

    # Test getting reviews for an item
    @task(2)
    def get_reviews_for_item(self):
        self.client.get("/reviews/item/11")

    # Test getting reviews for a user
    @task(3)
    def get_reviews_for_user(self):
        self.client.get("/reviews/user/tim")

    # Test updating a review
    # @task(4)
    # def update_review(self):
    #     updated_review_data = {
    #         "rating": 5,
    #         "comment": "Updated comment: Even better!"
    #     }
    #     # Replace `review_id` with an actual ID during testing
    #     self.client.put("/reviews/replace_with_review_id", json=updated_review_data)

    # # Test deleting a review
    # @task(5)
    # def delete_review(self):
    #     # Replace `review_id` with an actual ID during testing
    #     self.client.delete("/reviews/replace_with_review_id")
