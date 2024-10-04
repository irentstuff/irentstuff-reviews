from prometheus_client import Counter, Histogram, REGISTRY


# Helper function to check if a metric is already registered
def check_metric(metric_name):
    return any(
        [metric for metric in REGISTRY.collect()
            if metric.name == metric_name]
    )


# Define some metrics with checks to avoid duplicates
if not check_metric("django_request_count"):
    request_counter = Counter(
        "django_request_count",
        "Total number of requests"
    )


if not check_metric("django_request_latency_seconds"):
    request_latency = Histogram(
        "django_request_latency_seconds",
        "Request latency"
    )


if not check_metric("create_review_requests_total"):
    create_review_counter = Counter(
        "create_review_requests_total",
        "Total number of CreateReview requests",
        ["user_id", "item_id"],
    )

if not check_metric("create_review_latency_seconds"):
    create_review_latency = Histogram(
        "create_review_latency_seconds", "Latency for CreateReview requests"
    )

if not check_metric("get_reviews_latency_seconds"):
    get_reviews_latency = Histogram(
        "get_reviews_latency_seconds", "Latency for GetReviewsForItem requests"
    )

if not check_metric("update_review_latency_seconds"):
    update_review_latency = Histogram(
        "update_review_latency_seconds", "Latency for updating a review"
    )

if not check_metric("delete_review_latency_seconds"):
    delete_review_latency = Histogram(
        "delete_review_latency_seconds", "Latency for deleting a review"
    )

if not check_metric("unauthorized_access_total"):
    unauthorized_access_counter = Counter(
        "unauthorized_access_total",
        "Total number of unauthorized access attempts"
    )

if not check_metric("api_errors_total"):
    api_error_counter = Counter(
        "api_errors_total",
        "Total number of API errors by status code",
        ["status_code"]
    )

if not check_metric("successful_requests_total"):
    successful_request_counter = Counter(
        "successful_requests_total", "Total number of successful requests"
    )

if not check_metric("reviews_fetched_total"):
    reviews_fetched_counter = Counter(
        "reviews_fetched_total",
        "Total number of reviews fetched per item",
        ["item_id"]
    )


# --- Utility functions ---
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
