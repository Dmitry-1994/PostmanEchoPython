import requests
class APIClient:
    base_url = "https://postman-echo.com"

    def send_get(self):
        response = requests.get(f'{self.base_url}/get')
        return response

    def send_get_with_params(self, params):
        response = requests.get(f'{self.base_url}/get', params=params)
        return response

    def send_invalid_get(self):
        response = requests.post(f'{self.base_url}/get')
        return response

    def send_post_with_params_body_headers(self, params, body, headers):
        response = requests.post(f'{self.base_url}/post', params=params, json=body, headers=headers)
        return response

    def send_invalid_post(self):
        response = requests.delete(f'{self.base_url}/post')
        return response