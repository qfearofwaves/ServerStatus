import requests
import time

class StatusClient:
    def __init__(self, base_url, retry_interval=2):
        self.base_url = base_url
        self.retry_interval = retry_interval

    def get_status(self):
        while True:
            try:
                response = requests.get(f"{self.base_url}/status")
                response.raise_for_status()
                data = response.json()
                if data["result"] != "pending":
                    return data["result"]
                time.sleep(self.retry_interval)
            except requests.RequestException as e:
                print(f"Request failed: {e}")
                time.sleep(self.retry_interval)

# Usage
client = StatusClient("http://127.0.0.1:5000")
print(client.get_status())
