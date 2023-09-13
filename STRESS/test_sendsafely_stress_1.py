# pip install locust
# http://localhost:8089/
# locust -f test_sendsafely_stress_1.py --host http://localhost:3000 --users 5000 --spawn-rate 20
# locust -f test_sendsafely_stress_1.py

from locust import HttpUser, task, between

class MyUser(HttpUser):
    # Set the wait time between requests (in seconds)
    wait_time = between(1, 3)  # Random wait time between 1 and 3 seconds

    @task
    def my_task(self):
        # Define the HTTP GET request you want to simulate
        response = self.client.get("https://www.sendsafely.com")

        # You can check the response status code or content if needed
        if response.status_code == 200:
            self.locust.log_success("GET request succeeded", response.elapsed.total_seconds())
        else:
            self.locust.log_failure("GET request failed", response.status_code)



