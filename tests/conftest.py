import pytest

base_url = "https://postman-echo.com"

@pytest.fixture()
def get_base_url():
    return base_url

@pytest.fixture()
def get_valid_params():
    params = {"name": "Dima", "card_id": 123}
    return params

@pytest.fixture()
def get_valid_body_data():
    body_data = {"card_name": "T", "balance": 1}
    return body_data

@pytest.fixture()
def get_valid_headers_data():
    headers_data = {"Content-Type": "application/json"}
    return headers_data