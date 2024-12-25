import requests
import json

BASE_URL = 'http://localhost:8000/api'

def test_endpoints():
    # 1. Register a new user
    register_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    }
    response = requests.post(f'{BASE_URL}/users/register/', json=register_data)
    print("Register:", response.status_code)

    # 2. Get JWT token
    token_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    response = requests.post(f'{BASE_URL}/token/', json=token_data)
    token = response.json()['access']
    headers = {'Authorization': f'Bearer {token}'}
    print("Token:", response.status_code)

    # 3. Create a category
    category_data = {"name": "Electronics"}
    response = requests.post(f'{BASE_URL}/categories/', 
                           json=category_data, 
                           headers=headers)
    category_id = response.json()['id']
    print("Create category:", response.status_code)

    # 4. Create a product
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": "99.99",
        "category_id": category_id,
        "stock_quantity": 10
    }
    response = requests.post(f'{BASE_URL}/products/', 
                           json=product_data, 
                           headers=headers)
    product_id = response.json()['id']
    print("Create product:", response.status_code)

    # 5. Add to wishlist
    response = requests.post(f'{BASE_URL}/products/{product_id}/add-to-wishlist/', 
                           headers=headers)
    print("Add to wishlist:", response.status_code)

    # 6. Get wishlist
    response = requests.get(f'{BASE_URL}/wishlist/', headers=headers)
    print("Get wishlist:", response.status_code)

if __name__ == "__main__":
    test_endpoints() 