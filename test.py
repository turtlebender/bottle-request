import unittest
import bottle
import  bottle_request

class TestRequestPlugin(unittest.TestCase):

    def setUp(self):
        self.app = bottle.Bottle(catchall=False)

    def test_with_keyword(self):
        self.plugin = self.app.install(bottle_request.Plugin)

        @self.app.get('/')
        def test(request, response):
            self.assertEqual(bottle.request, request)
            self.assertEqual(bottle.response, response)
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x, y: None)

    def test_without_keyword(self):
        self.plugin = self.app.install(bottle_request.Plugin)

        @self.app.get('/')
        def test():
            pass
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x, y: None)
