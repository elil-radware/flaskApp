from app.basicServer import app
import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/books/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
#
#     def test_database_books(self):
#         tester = os.path.exists("database.db")
#         self.assertTrue(tester)


if __name__ == '__main__':
    unittest.main()
    # unittest.TestResult()