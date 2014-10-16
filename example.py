#!/usr/bin/python

import subprocess
import psycopg2

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

class SqlInteraction:

	def add_uptime_seconds(self):
		_conn = psycopg2.connect("dbname=facterstore user=ryan")
		_cursor = _conn.cursor()
		_facter_data_dictionary = FacterPoller().get_facter_data_dictionary()

		_cursor.execute("INSERT INTO facterstats VALUES (%s, %s)", [_facter_data_dictionary['uptime_seconds'], _facter_data_dictionary['memoryfree_mb']])
		_conn.commit()

		_cursor.close()
		_conn.close()

if __name__ == "__main__":
	SqlInteraction().add_uptime_seconds()