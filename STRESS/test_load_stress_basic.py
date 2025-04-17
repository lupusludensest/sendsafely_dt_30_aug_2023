# Basic load testing script for web applications using Locust
# For setup and usage instructions, see README.md in this directory

from locust import HttpUser, task, between

class MyUser(HttpUser):
    # Set the wait time between requests (in seconds)
    wait_time = between(1, 3)  # Random wait time between 1 and 3 seconds

    @task
    def my_task(self):
        # Define the HTTP GET request you want to simulate
        # The base URL will be taken from the --host parameter
        response = self.client.get("/")

        # You can check the response status code or content if needed
        if response.status_code == 200:
            self.locust.log_success("GET request succeeded", response.elapsed.total_seconds())
        else:
            self.locust.log_failure("GET request failed", response.status_code)



