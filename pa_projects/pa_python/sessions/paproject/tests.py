import unittest

from pyramid import testing

class ProjectViewTests(unittest.TestCase):
	def setUp(self):
		self.config=testing.setUp()

	def tearDown(self):
		testing.tearDown()



	def test_home(self):
		from .views import projectviews 
	
		request=testing.DummyRequest()
		inst=projectviews(request)
		response=inst.home()
		self.assertEqual('Home View',response['name'])


	def test_hello(self):
		from .views import projectviews 
	
		request=testing.DummyRequest()
		inst=projectviews(request)
		response=inst.hello()
		self.assertEqual('Hello View',response['name'])

	

class ProjectFunctionalTests(unittest.TestCase):
	def setUp(self):
		from paproject import main
		app=main({})
		from webtest import TestApp

		self.testapp=TestApp(app)


	def test_home(self):
		res=self.testapp.get('/',status=200)
		self.assertIn(b'<h1>Hi Home View',res.body)


	def test_hello(self):
		res=self.testapp.get('/howdy',status=200)
		self.assertIn(b'<h1>Hi Hello View',res.body)
