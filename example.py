#!/usr/bin/python

import subprocess

class FacterPoller:

	def get_facter_data_string(self):

		_facter_data_string = subprocess.check_output(["facter"])
		return _facter_data_string

	def get_facter_data_list(self):

		#this works and removes empty lines, but i googled the solution and cannot yet follow the logic.
		return [line for line in self.get_facter_data_string().split('\n') if line.strip() != '']

	def get_facter_data_dictionary(self):

		_facter_data_dictionary = {}

		for item in self.get_facter_data_list():
			_key, _value = item.split(' => ')
			_facter_data_dictionary[_key] = _value

		return _facter_data_dictionary
