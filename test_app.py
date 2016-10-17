import unittest
from app import app


class DbServer(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_set_get(self):
        set_response = requests.get(BASE_URL + '/set?key1=val1')
        self.assertEqual(200, set_response.status_code)
        get_response = requests.get(BASE_URL + '/get?key=key1')
        self.assertEqual(200, get_response.status_code)
        self.assertEqual('val1', get_response.text)

if __name__ == '__main__':
    unittest.main()
