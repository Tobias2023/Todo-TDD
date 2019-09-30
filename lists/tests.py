from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertIn('<title>To-Do list</title>',
        response.content.decode()
        )
        self.assertTrue(response.content.decode().endswith('</html>'))
