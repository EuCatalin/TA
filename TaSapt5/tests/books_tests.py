import unittest

from request_apis.books_api import BookApi


class BooksTests(unittest.TestCase):

    accessToken = ''

    def setUp(self) -> None:
        self.books = BookApi()
        if self.accessToken == '':
            self.accessToken = self.books.post_api_clients().json()['accessToken']

    def test_books_status(self):

        response = self.books.get_api_status()
        self.assertEqual(response.status_code, 200, "Status code is not the same")
        self.assertEqual(response.json()['status'], "OK", "Response status is not the same")

    def test_books_all_books(self):

        response = self.books.get_api_books_filter()
        self.assertEqual(response.status_code, 200, "Status code is not the same")

        expected_number = 6
        self.assertEqual(len(response.json()), expected_number, "Number of books is not the same")
        self.assertEqual(response.json()[0]["id"], 1, "Id of the first book is not the same")

    def test_books_by_fiction_type(self):
        response = self.books.get_api_books_filter(book_type="fiction")
        book_list = response.json()

        self.assertEqual(response.status_code, 200, "Status code is not the same")

        expected_type = 'fiction'

        for book in book_list:
            self.assertEqual(book['type'], expected_type, "Expected type is not fiction")

    def test_books_by_nonfiction_type(self):
        response = self.books.get_api_books_filter(book_type="non-fiction")
        book_list = response.json()
        print(book_list)
        self.assertEqual(response.status_code, 200, "Status code is not the same")

        expected_type = 'non-fiction'

        for book in book_list:
            self.assertEqual(book['type'], expected_type, "Expected type should be non-fiction")

    def test_books_by_invalid_type(self):
        response = self.books.get_api_books_filter(book_type="aasdasd")
        expected_status_code = 400
        expected_response = {'error': "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."}

        self.assertEqual(response.status_code, 400, "Status code is not the same")
        self.assertEqual(response.json(), expected_response, "Response message is not the same")


    #todo test_books_by_id()
    def test_books_by_id(self):
        response = self.books.get_api_books_filter()
        random_book_id = response.json()[0]["id"]
        expected_book_name = response.json()[0]["name"]
        availability_book = response.json()[0]["available"]

        response = self.books.get_api_book_by_id(random_book_id)
        self.assertEqual(response.status_code, 200, "Status code is not the same")
        self.assertEqual(response.json()["id"], random_book_id, "Book id is not the same")
        self.assertEqual(response.json()["name"], expected_book_name, "Book name is not the same")
        self.assertEqual(response.json()["available"], availability_book, "Book's availability is not the same")

    def test_books_filtered(self):
        response = self.books.get_api_books_filter(book_type="fiction", limit="4")
        expected_number = 4
        self.assertEqual(len(response.json()), expected_number, "Number of books is not the same")

    def test_books_by_invalid_superior_limit(self):
        response = self.books.get_api_books_filter(limit=15)
        print(response.json())
        expected_status_code = 400
        expected_response_message = {'error': "Invalid value for query parameter 'limit'. Cannot be greater than 20."}

        self.assertEqual(response.status_code, expected_status_code, "Status code is not the same")
        self.assertEqual(response.json(),
                         expected_response_message,
                         f"Response mesage is not the same. " +
                         f"\nExpected {expected_response_mesage} \n Got: {response.json}")

    def test_books_by_invalid_inferior_limit(self):
        response = self.books.get_api_books_filter(limit=-1)

        expected_response_message = {'error': "Invalid value for query parameter 'limit'. Must be greater than 0."}
        self.assertEqual(expected_response_message,
                         f"Response message is not the same. " +
                         f"\nExpected {expected_response_message} \n Got: {response.json}")

    def test_books_orders(self):
        response = self.books.get_books_orders(self.accessToken)
        self.assertEqual(response.status_code, 200, "Status code is not the same")
        expected_number = 0
        self.assertEqual(len(response.json()), expected_number, "Number of orders is not the same")

    def test_books_by_limit(self):
        response = self.books.get_api_books_filter(limit=4)
        book_list = response.json()
        expected_length = 4

        self.assertEqual(response.status_code, expected_status_code, "Status code is not the same")

    def test_books_by_zero_limit(self):
        response = self.books.get_api_books_filter(limit=0)
        book_list = response.json()
        expected_length = 6

       # self.assertEqual(len(response., expected_status_code, "Status code is not the same")!!!!!

    def test_valid_authentication(self):
        response = self.books.post_api_client("test", "test@web.com")
        print(response.json())
        expected_status_code = 201
        self.assertEqual(expected_status_code, response.status_code, "Status code is not the same")
        


    #todo test_books_order_cu_token_invalid
    def test_books_order_invalid_token(self):
        pass

    def test_books_order_by_id(self):
        pass

    def test_books_post_order(self):
        pass

    def test_books_patch_order(self):
        pass

    def test_books_delete_invalid_order(self):
        pass

    def test_books_delete_personal_order(self):
        pass