import pytest
import requests
from jsonschema import validate

from schemas import (get_list_user_schema, get_single_user_schema, get_list_resource_schema, create_user_schema,
                     update_put_user_schema, update_patch_user_schema)

BASE_URL = "http://127.0.0.1:8000"


@pytest.mark.parametrize("page_number", [
    (2)
])
def test_api_list_users_status_code_200(page_number):
    # url = f"https://reqres.in/api/users?page={page_number}"
    url = f"{BASE_URL}/api/users?page={page_number}"
    response = requests.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize("page_number", [
    (2)
])
def test_api_list_users_response_not_empty(page_number):
    # url = f"https://reqres.in/api/users?page={page_number}"
    url = f"{BASE_URL}/api/users?page={page_number}"
    response = requests.get(url)
    data = response.json()
    assert len(data['data']) > 0


@pytest.mark.parametrize("page_number", [
    (2)
])
def test_api_list_users_validate_response_schema(page_number):
    # url = f"https://reqres.in/api/users?page={page_number}"
    url = f"{BASE_URL}/api/users?page={page_number}"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url, headers=headers)
    body = response.json()
    validate(body, get_list_user_schema)


@pytest.mark.parametrize("user_id", [
    (2)
])
def test_api_single_user_status_code_200(user_id):
    # url = f"https://reqres.in/api/users/{user_id}"
    url = f"{BASE_URL}/api/users/{user_id}"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


@pytest.mark.parametrize("user_id", [
    (2)
])
def test_api_single_user_validate_response_schema(user_id):
    # url = f"https://reqres.in/api/users/{user_id}"
    url = f"{BASE_URL}/api/users/{user_id}"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url, headers=headers)
    body = response.json()
    validate(body, get_single_user_schema)


def test_api_list_resource_status_code_200():
    # url = "https://reqres.in/api/unknown"
    url = f"{BASE_URL}/api/unknown"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


def test_api_list_resource_response_not_empty():
    # url = "https://reqres.in/api/unknown"
    url = f"{BASE_URL}/api/unknown"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url, headers=headers)
    data = response.json()
    assert len(data['data']) > 0


def test_api_list_resource_validate_response_schema():
    # url = "https://reqres.in/api/unknown"
    url = f"{BASE_URL}/api/unknown"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url, headers=headers)
    body = response.json()
    validate(body, get_list_resource_schema)


def test_api_create_user_status_code_201():
    response = requests.post(  # "https://reqres.in/api/users",
        f"{BASE_URL}/api/users",
        json={"name": "morpheus", "job": "leader"})
    assert response.status_code == 201


def test_api_create_user_validate_response_schema():
    response = requests.post(  # "https://reqres.in/api/users",
        f"{BASE_URL}/api/users",
        json={"name": "morpheus", "job": "leader"})
    body = response.json()
    validate(body, create_user_schema)


def test_api_create_user_attributes_match_expected_values():
    response = requests.post(  # "https://reqres.in/api/users"
        f"{BASE_URL}/api/users",
        json={"name": "morpheus", "job": "leader"})
    data = response.json()
    assert data['name'] == 'morpheus'
    assert data['job'] == 'leader'


@pytest.mark.parametrize("user_id", [
    (2)
])
def test_api_put_update_user_status_code_200(user_id):
    response = requests.put(  # "https://reqres.in/api/users/2",
        url=f"{BASE_URL}/api/users/{user_id}",
        json={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200


@pytest.mark.parametrize("user_id", [
    (2)
])
def test_api_put_update_user_validate_response_schema(user_id):
    response = requests.put(  # "https://reqres.in/api/users/2"
        url=f"{BASE_URL}/api/users/{user_id}",
        json={"name": "morpheus", "job": "zion resident"})
    body = response.json()
    validate(body, update_put_user_schema)


@pytest.mark.parametrize("user_id", [
    (2)
])
def test_api_patch_update_user_status_code_200(user_id):
    response = requests.patch(  # "https://reqres.in/api/users/2",
        url=f"{BASE_URL}/api/users/{user_id}",
        json={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200


@pytest.mark.parametrize("user_id", [
    (2)
])
def test_api_patch_update_user_validate_response_schema(user_id):
    response = requests.patch(  # "https://reqres.in/api/users/2",
        url=f"{BASE_URL}/api/users/{user_id}",
        json={"name": "morpheus", "job": "zion resident"})
    body = response.json()
    validate(body, update_patch_user_schema)


@pytest.mark.parametrize("user_id", [
    (2)
])
def test_api_delete_user_status_code_204(user_id):
    response = requests.delete(url=f"{BASE_URL}/api/users/{user_id}")
    assert response.status_code == 204
