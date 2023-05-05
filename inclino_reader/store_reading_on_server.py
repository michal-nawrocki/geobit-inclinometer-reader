import logging
import requests

logger = logging.getLogger(__name__)

BASE_URL = "http://inklinometry.geobitmn.pl:8000/"
HEADERS = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjo4ODA4MzE5NjAzMiwiaWF0IjoxNjgzMjgyNDMyLCJqdGkiOiJlOWE5Y2U0NDMyYTk0MGQ4YTZlNzYyY2VmM2EzOTFlYyIsInVzZXJfaWQiOjJ9.wAFIreb6cqxsEuKH5mTNra8lwPSbD7bpKazh1kjKk-Y'
}

def check_if_alive():
    # Check if the server is alive
    response = requests.get(
        url=f"{BASE_URL}healthcheck",
    )
    return response.status_code == 200

def store_reading_on_remote(value, sensor_id):
    payload = {
        "sensor": sensor_id,
        "value": value
    }
    
    response = requests.post(
        url=f"{BASE_URL}api/readings/",
        headers=HEADERS,
        data=payload)
    
    print(f"Response data: {response.json()}")
    return response.status_code == 201

if __name__ == "__main__":
    try:
        assert check_if_alive()
    except AssertionError:
        logging.info("Server at {BASE_URL} seems to not be working. Won't store latest result...")
