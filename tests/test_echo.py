import requests

from api_client import APIClient
from helpers import check_status_code, check_json_data

# base_url = "https://postman-echo.com"
# params = {"name": "Dima", "card_id": 123}
# body_data = {"card_name": "T", "balance": 1}
# headers_data = {"Content-Type": "application/json"}


def test_get_request(get_base_url):
    client = APIClient()
    response = client.send_get()
    # response = requests.get(f'{base_url}/get')
    # assert response.status_code == 200
    check_status_code(response, 200)
    base_url = get_base_url
    # assert response.json()["headers"]["host"] == base_url.split("/")[-1]
    check_json_data(response.json()["headers"]["host"], base_url.split("/")[-1])

def test_get_request_with_params(get_valid_params):
    client = APIClient()
    params = get_valid_params
    # response = requests.get(f'{base_url}/get', params=params)
    response = client.send_get_with_params(params)
    # assert response.status_code == 200
    check_status_code(response, 200)
    # data = response.json()
    expected_data = {key: str(value) for key, value in params.items()}
    # assert data["args"] == expected_data
    check_json_data(response.json()["args"], expected_data)

def test_post_request_send_get():
    client = APIClient()
    # response = requests.post(f'{base_url}/get')
    response = client.send_invalid_get()
    # assert response.status_code == 404
    check_status_code(response, 404)

def test_post_request_with_params_body(get_valid_params, get_valid_body_data, get_valid_headers_data):
    client = APIClient()
    params = get_valid_params
    body_data = get_valid_body_data
    headers_data = get_valid_headers_data
    # response = requests.post(f'{base_url}/post', params=params, json=body_data, headers=headers_data)
    response = client.send_post_with_params_body_headers(params, body_data, headers_data)
    check_status_code(response, 200)
    # data = response.json()
    expected_args = {key: str(value) for key, value in params.items()}
    # print(data["args"])
    # assert data["args"] == expected_args
    check_json_data(response.json()["args"], expected_args)
    # assert data["data"] == body_data
    check_json_data(response.json()["data"], body_data)
    # assert data["headers"]["content-type"] == headers_data["Content-Type"]
    check_json_data(response.json()["headers"]["content-type"], headers_data["Content-Type"])

def test_delete_request_send_post():
    client = APIClient()
    # response = requests.delete(f'{base_url}/post')
    response = client.send_invalid_post()
    check_status_code(response, 404)



