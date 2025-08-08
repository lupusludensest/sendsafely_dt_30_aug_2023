# Basic load testing script for web applications using Locust
# For setup and usage instructions, see README.md in this directory

from locust import HttpUser, task, between

class MyUser(HttpUser):
    # Set the wait time between requests (in seconds)
    wait_time = between(1, 3)  # Random wait time between 1 and 3 seconds

    @task
    def my_task(self):
        try:
            # Check if the 'request_failure' attribute exists
            if hasattr(self.environment.events, "request_failure"):
                print("request_failure attribute exists in events.")
            else:
                print("request_failure attribute does NOT exist in events.")

            # Define the HTTP GET request you want to simulate
            response = self.client.get("/")

            # Log success or failure using Locust's built-in methods
            if response.status_code == 200:
                self.environment.events.request_success.fire(
                    request_type="GET",
                    name="/",
                    response_time=response.elapsed.total_seconds(),
                    response_length=len(response.content),
                )
            else:
                self.environment.events.request_failure.fire(
                    request_type="GET",
                    name="/",
                    response_time=response.elapsed.total_seconds(),
                    response_length=len(response.content),
                    exception=Exception(f"GET request failed with status code {response.status_code}"),
                )
        except Exception as e:
            self.environment.events.request_failure.fire(
                request_type="GET",
                name="/",
                response_time=0,
                response_length=0,
                exception=e,
            )



