#!/usr/bin/python

import unittest

#from example import ExampleClass
from example import FacterPoller

'''
class ExampleTests(unittest.TestCase):

	def test_first(self):
		self.assertTrue(ExampleClass().return_true())
'''

class HarvestFacterDataTests(unittest.TestCase):

	__facter_data_string = FacterPoller().harvest_facter_data()

	def test_not_null(self):
		self.assertNotEqual(self.__facter_data_string, None)

	def test_is_a_str(self):
		self.assertIsInstance(self.__facter_data_string, str)

class SplitFacterDataIntoListTests(unittest.TestCase):

	__facter_data_list = FacterPoller().get_facter_data_list()

	def test_not_null(self):
		self.assertNotEqual(self.__facter_data_list, None)
#		self.assertNotEqual(self.__facter_data_list[0], None)
#		self.assertNotEqual(self.__facter_data_list[-1], None)

	def test_is_a_list(self):
		self.assertIsInstance(self.__facter_data_list, list)

	def test_is_sane_size(self):
		self.assertTrue(len(self.__facter_data_list) > 10)

	def test_data_contents_are_sane(self):
		self.assertIn("architecture", self.__facter_data_list[0])
		self.assertIn("uptime ", self.__facter_data_list[-5])
		self.assertIn("virtual", self.__facter_data_list[-1])


if __name__ == '__main__':
    unittest.main()