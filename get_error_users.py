#! /usr/bin/env python

import sys
from commons import write_dict_data_to_csv_file

def get_error_users_from_log(log_path):
	text_file = open(log_path, 'rb')
	data = text_file.read()
	text_file.close()
	
	error_users = []
	
	lines = data.split('\n')
	for line in lines:
		if 'Update IMAP for user' in line:
			tmp = line.split(' ')
			if tmp[4]:
				error_user = {'error_user':tmp[4]}
				error_users.append(error_user)
				
	return error_users
	

def export_error_users_from_log(log_path, csv_path):
	error_users = get_error_users_from_log(log_path)
	write_dict_data_to_csv_file(csv_path, error_users)
	
	
	
if __name__ == "__main__":
	log_path = sys.argv[1]
	csv_path = sys.argv[2]
	export_error_users_from_log(log_path, csv_path)
