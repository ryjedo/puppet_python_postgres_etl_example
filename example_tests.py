#!/usr/bin/python

import unittest

from example import FacterPoller

class HarvestFacterDataTests(unittest.TestCase):

	__facter_data_string = FacterPoller().get_facter_data_string()

	def test_not_null(self):
		self.assertNotEqual(self.__facter_data_string, None)

	def test_is_a_str(self):
		self.assertIsInstance(self.__facter_data_string, str)

class SplitFacterDataIntoListTests(unittest.TestCase):

	__facter_data_list = FacterPoller().get_facter_data_list()

	def test_not_null(self):
		self.assertNotEqual(self.__facter_data_list, None)

	def test_is_a_list(self):
		self.assertIsInstance(self.__facter_data_list, list)

	def test_is_sane_size(self):
		self.assertTrue(len(self.__facter_data_list) > 10)

	def test_data_contents_are_sane(self):
		self.assertIn("architecture", self.__facter_data_list[0])
		self.assertIn("uptime ", self.__facter_data_list[-5])
		self.assertIn("virtual", self.__facter_data_list[-1])

class ConvertListIntoDictionaryTests(unittest.TestCase):

	__facter_data_dictionary = FacterPoller().get_facter_data_dictionary()
	__facter_data_list = FacterPoller().get_facter_data_list()

	def test_not_null(self):
		self.assertNotEqual(self.__facter_data_dictionary, None)

	def test_is_a_list(self):
		self.assertIsInstance(self.__facter_data_dictionary, dict)

	def test_dict_is_same_size_as_source_list(self):
		self.assertEqual(len(self.__facter_data_list), len(self.__facter_data_dictionary))

	def test_data_contents_are_sane(self):
		self.assertNotEqual(self.__facter_data_dictionary['architecture'], "")
		self.assertNotEqual(self.__facter_data_dictionary['architecture'], None)
		self.assertNotEqual(self.__facter_data_dictionary['virtual'], "")
		self.assertNotEqual(self.__facter_data_dictionary['virtual'], None)
		self.assertNotEqual(self.__facter_data_dictionary['puppetversion'], "")
		self.assertNotEqual(self.__facter_data_dictionary['puppetversion'], None)

if __name__ == '__main__':
    unittest.main()