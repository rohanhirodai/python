import unittest

from pyramid import testing


class PaprojectViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import PaprojectViews

        request = testing.DummyRequest()
        inst = PaprojectViews(request)
        response = inst.home()
        self.assertEqual('Home View', response['page_title'])

    def test_hello(self):
        from .views import PaprojectViews

        request = testing.DummyRequest()
        inst = PaprojectViews(request)
        response = inst.hello()
        self.assertEqual('Hello View', response['page_title'])


class PaprojectFunctionalTests(unittest.TestCase):
    def setUp(self):
        from paproject import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'PaprojectViews - Home View', res.body)

    def test_hello(self):
        res = self.testapp.get('/howdy/{first}/{last}', status=200)
        self.assertIn(b'PaprojectViews - Hello View', res.body)

    def test_css(self):
        res = self.testapp.get('/static/app.css', status=200)
        self.assertIn(b'body', res.body)
