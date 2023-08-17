import requests
import random

class BookApi:

    _BASE_URL = "https://simple-books-api.glitch.me"
    _API_CLIENTS_ENDPOINT = "/api-clients/"
    _BOOKS_ENDPOINT = "/books"
    _ORDERS_ENDPOINT = "/orders"
    _STATUS_ENDPOINT = "/status"

    def get_api_status(self):
        URL = self._BASE_URL + self._STATUS_ENDPOINT
        return requests.get(URL)

    def get_api_books_filter(self, book_type="", limit=""):
        URL = self._BASE_URL + self._BOOKS_ENDPOINT

        query_params = {
            "type": book_type,
            "limit": limit
        }

        return requests.get(URL, params=query_params)

    def get_api_book_by_id(self, book_id):
        URL = self._BASE_URL + self._BOOKS_ENDPOINT + f"/{book_id}"
        return requests.get(URL)

    def post_api_clients(self):
        URL = self._BASE_URL + self._API_CLIENTS_ENDPOINT

        random_number = random.randint(1, 9999999999999999999)

        body = {
            "clientName": "PYTA4",
            "clientEmail": f"pyta-test{random_number}@web.com"
        }

        response = requests.post(URL, json=body)

        return response

    def get_books_orders(self, access_token):
        URL = self._BASE_URL + self._ORDERS_ENDPOINT

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        return requests.get(URL, headers=headers)

    #todo get_book_by_id(self, id)