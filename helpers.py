def check_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code

def check_json_data(response, expected):
    assert response == expected