import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

def test_create_users(): # проверка на наличие пользователей
    resp = requests.post(f"{BASE_URL}/user", json={"id": 1, "username": "amin", "firstName": "John", "lastName": "Doe"})

    assert resp.status_code == 200


def test_get_users():
    resp = requests.get(f"{BASE_URL}/user/admin")

    assert resp.status_code == 200

def test_delete_users():
    resp = requests.delete(f"{BASE_URL}/user/admin")

    assert resp.status_code == 200