#!/usr/bin/python

import subprocess

class FacterPoller:

	def harvest_facter_data(self):

		_facter_data = subprocess.check_output(["facter"])
		return _facter_data

	def get_facter_data_list(self):

		#this works and removes empty lines, but i googled the solution and cannot yet follow the logic.
		return [line for line in self.harvest_facter_data().split('\n') if line.strip() != '']
