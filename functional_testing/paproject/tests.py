import unittest

from pyramid import testing

class ProjectViewTests(unittest.TestCase):
	def setUp(self):
		self.config=testing.setUp()

	def tearDown(self):
		testing.tearDown()

	def test_hello_world(self):
		from paproject import hello_world
	
		request=testing.DummyRequest()
		response=hello_world(request)
		self.assertEqual(response.status_code,200)



class ProjectFunctionalTests(unittest.TestCase):
	def setUp(self):
		from paproject import main
		app=main({})
		from webtest import TestApp

		self.testapp=TestApp(app)

	def test_hello_world(self):
		res=self.testapp.get('/',status=200)
		self.assertIn(b'<h1>Hello World!</h1>',res.body)
