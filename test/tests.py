import unittest
from meninascomp import app

class TestIndex(unittest.TestCase):

    def setUp(self):
        app_test = app.test_client()
        self.response = app_test.get('/')

    def testaPaginaHome200(self):
        self.assertEqual(200, self.response.status_code)

    def testContentType(self):
        self.assertIn('text/html', self.response.content_type)

    def testBootstrapCSS(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

if __name__ == '__main__':
    unittest.main()
