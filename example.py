#!/usr/bin/python

import subprocess

'''
class ExampleClass:

	def return_true(self):
		return True
'''

class FacterPoller:

	def harvest_facter_data(self):

		_facter_data = subprocess.check_output(["facter"])
		return _facter_data

	def get_facter_data_list(self):

		#_facter_data_list = self.harvest_facter_data().split('\n')
		return [line for line in self.harvest_facter_data().split('\n') if line.strip() != '']

		#return _facter_data_list