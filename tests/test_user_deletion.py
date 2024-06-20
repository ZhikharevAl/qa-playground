import requests
import pytest
from dotenv import load_dotenv
import os

load_dotenv()
auth_token = os.getenv('AUTH_TOKEN')

BASE_URL_RELEASE = "https://release-gs.qa-playground.com/api/v1"
BASAE_URL_DEV = "https://dev-gs.qa-playground.com/api/v1"
AUTH_HEADER = {
    "Authorization": f"Bearer {auth_token}",
}

def headers(x_task_id):
    return {
        "Authorization": AUTH_HEADER["Authorization"],
        "X-Task-Id": x_task_id
    }

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    response = requests.post(f"{BASE_URL_RELEASE}/setup", headers=AUTH_HEADER)
    assert response.status_code == 205

@pytest.mark.parametrize("base_url", [BASE_URL_RELEASE, BASAE_URL_DEV])
def test_delete_user(base_url):
    x_task_id = "API-1"
    
    response = requests.get(f"{base_url}/users", headers=headers(x_task_id))
    assert response.status_code == 200
    data = response.json()
    
    assert "users" in data, "Key 'users' not found in response"
    
    users = data["users"]
    assert isinstance(users, list), "'users' is not a list"
    assert len(users) > 0, "No users found"
    
    user_uuid = users[0]["uuid"]

    response = requests.delete(f"{base_url}/users/{user_uuid}", headers=headers(x_task_id))
    assert response.status_code == 204

    response = requests.get(f"{base_url}/users", headers=headers(x_task_id))
    assert response.status_code == 200
    data = response.json()
    users = data["users"]

    assert not any(user["uuid"] == user_uuid for user in users), "User not deleted"

    response = requests.get(f"{base_url}/users/{user_uuid}", headers=headers(x_task_id))
    assert response.status_code == 404