import app
import re
import unittest

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.client = app.app.test_client()

    def test_root(self):
        rv = self.client.get('/')
        assert rv.status_code == 200

        message = rv.data.decode()
        start = re.search("<h1>", message).start()
        end = re.search("</h1>", message).start()
        message = message[start+4:end]

        assert message == "hello brother, Lets have some fun!!"

    def test_name(self):
        name = 'alice'
        rv = self.client.get(f'/{name}')
        assert rv.status_code == 200

        message = rv.data.decode()
        start = re.search("<h1>", message).start()
        end = re.search("</h1>", message).start()
        message = message[start+4:end]

        assert message == "alice: A nerd"