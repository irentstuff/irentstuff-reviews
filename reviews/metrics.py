from prometheus_client import Counter, Histogram

# Define some metrics
request_counter = Counter('django_request_count', 'Total number of requests')
request_latency = Histogram('django_request_latency_seconds', 'Request latency')
create_review_counter = Counter(
    'create_review_requests_total', 
    'Total number of CreateReview requests',
    ['user_id', 'item_id']  # Adding labels for user and item
)

create_review_latency = Histogram('create_review_latency_seconds', 'Request latency for CreateReview')

get_reviews_latency = Histogram('get_reviews_latency_seconds', 'Latency for GetReviewsForItem')
update_review_latency = Histogram('update_review_latency_seconds', 'Latency for updating a review')
delete_review_latency = Histogram('delete_review_latency_seconds', 'Latency for deleting a review')
unauthorized_access_counter = Counter('unauthorized_access_total', 'Total unauthorized access attempts')

def increment_create_review_counter(user_id, item_id):
    create_review_counter.labels(user_id=user_id, item_id=item_id).inc()


def record_request_latency(latency):
    request_latency.observe(latency)

def increment_error_count(status_code):
    api_error_counter.labels(status_code=status_code).inc()

def increment_successful_request_count():
    successful_request_counter.inc()

def increment_reviews_fetched(item_id, count):
    reviews_fetched_counter.labels(item_id=item_id).inc(count)

def increment_unauthorized_access():
    unauthorized_access_counter.inc()


# Define a metric for tracking error responses by status code
api_error_counter = Counter(
    'api_errors_total', 
    'Total number of API errors by status code',
    ['status_code']
)

def increment_error_count(status_code):
    api_error_counter.labels(status_code=status_code).inc()

# Define a counter for successful requests
successful_request_counter = Counter(
    'successful_requests_total', 
    'Total number of successful requests'
)

def increment_successful_request_count():
    successful_request_counter.inc()


# Define a counter for the number of reviews fetched
reviews_fetched_counter = Counter(
    'reviews_fetched_total', 
    'Total number of reviews fetched per item',
    ['item_id']
)

def increment_reviews_fetched(item_id, count):
    reviews_fetched_counter.labels(item_id=item_id).inc(count)
