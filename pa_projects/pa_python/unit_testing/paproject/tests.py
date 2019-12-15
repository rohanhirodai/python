import unittest

from pyramid import testing

class ProjectViewTests(unittest.TestCase):
	def setup(self):
		self.config=testing.setup()

	def tearDown(self):
		testing.tearDown()

	def test_hello_world(self):
		from paproject import hello_world
	
		request=testing.DummyRequest()
		response=hello_world(request)
		self.assertEqual(response.status_code,200)
