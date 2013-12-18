#! /usr/bin/env python

import sys
from commons import *


def print_proc_users(csv_path, condition_number):
	csv_dat = get_dict_data_from_csv_file(csv_path)
	if csv_dat:
		print "Processing user with condition %s\n" % condition_number
		for email in csv_dat:
			num = str_to_num(email['src']) % 10
			if num in condition_number or condition_number[0]==-1:
				print "%s to %s\n" % (email['src'], email['dest'])



if __name__ == "__main__":
	csv_path = sys.argv[1]
	if sys.argv[2] == 'all':
		condition_number = [-1]
	else:
		condition_number = map(int, sys.argv[2].split(','))

	print_proc_users(csv_path, condition_number)
