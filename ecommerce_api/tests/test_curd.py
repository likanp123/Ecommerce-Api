import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def client():
    user = User.objects.create_user(username='test', password='pass')
    client = APIClient()
    response = client.post('/api/token/', {'username': 'test', 'password': 'pass'})
    token = response.data['access']
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    return client

def test_create_product(client):
    response = client.post('/api/products/', {
        "name": "P1", "sku": "sku123", "price": 100, "inventory_count": 10, "source_platform": "shopify"
    })
    assert response.status_code == 201
