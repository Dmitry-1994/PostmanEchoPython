from api_client import APIClient
from helpers import check_status_code, check_json_data

invalid_body_data = {"card_name": "T", "balance": 10}

def test_get_request(get_base_url):
    client = APIClient()
    response = client.send_get()
    check_status_code(response, 200)
    base_url = get_base_url
    check_json_data(response.json()["headers"]["host"], base_url.split("/")[-1])

def test_get_request_with_params(get_valid_params):
    client = APIClient()
    params = get_valid_params
    response = client.send_get_with_params(params)
    check_status_code(response, 200)
    expected_data = {key: str(value) for key, value in params.items()}
    check_json_data(response.json()["args"], expected_data)

def test_post_request_send_get():
    client = APIClient()
    response = client.send_invalid_get()
    check_status_code(response, 404)

def test_post_request_with_params_body(get_valid_params, get_valid_body_data, get_valid_headers_data):
    client = APIClient()
    params = get_valid_params
    body_data = get_valid_body_data
    headers_data = get_valid_headers_data
    response = client.send_post_with_params_body_headers(params, body_data, headers_data)
    check_status_code(response, 200)
    expected_args = {key: str(value) for key, value in params.items()}
    check_json_data(response.json()["args"], expected_args)
    check_json_data(response.json()["data"], invalid_body_data)
    check_json_data(response.json()["headers"]["content-type"], headers_data["Content-Type"])

def test_delete_request_send_post():
    client = APIClient()
    response = client.send_invalid_post()
    check_status_code(response, 404)



