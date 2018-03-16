import os
import flaskr
import unittest
import tempfile

class FlaskTestCase(unittest.TestCase):
	def setUp():
		self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
		flakr.app.testing = True
		self.app = flaskr.app.test_client()
	def tearDown():
