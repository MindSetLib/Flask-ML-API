from locust import HttpUser, task
from request_testing import test_request


class PredictInsolver(HttpUser):
    @task
    def test_insolver(self):
        self.client.post("", json=test_request)