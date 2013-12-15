#! /usr/bin/env python
import csv
from os import listdir, rename
from os.path import isfile, join




def get_files_list(path):
	return [ f for f in listdir(path) ]


def get_username_list_from_text(username_file_path):
	# username_list = []
	text_file = open(username_file_path, 'rb')
	username_list = text_file.read()
	text_file.close()
	username_list = username_list.split('\n')
	return username_list


def get_email_list_from_text(file_path):
	text_file = open(file_path, 'rb')
	data = text_file.read()
	text_file.close()
	
	data = data.split('\n')
	email_list = []
	for line in data:
		if line:
			tmp = line.split(',')
			if len(tmp)==2:
				email_pair = {'src_email': tmp[0], 'dest_email': tmp[1]}
				email_list.append(email_pair)
	return email_list


# utilities
def get_dict_data_from_csv_file(csv_file_path):
	csv_file = open(csv_file_path, 'rb')
	csv_file.seek(0)
	sniffdialect = csv.Sniffer().sniff(csv_file.read(10000), delimiters='\t,;')
	csv_file.seek(0)
	#~ dialect = csv.excel
	dict_reader = csv.DictReader(csv_file, dialect=sniffdialect)
	csv_file.seek(0)
	dict_data = []
	for record in dict_reader:
		dict_data.append(record)

	csv_file.close()

	return dict_data


def write_dict_data_to_csv_file(csv_file_path, dict_data):
	csv_file = open(csv_file_path, 'wb')
	writer = csv.writer(csv_file, dialect='excel')
	
	headers = dict_data[0].keys()
	writer.writerow(headers)

	# headers must be the same with dat.keys()
	for dat in dict_data:
		line = []
		for field in headers:
			line.append(dat[field])
		writer.writerow(line)
		
	csv_file.close()


def str_to_num(input_str):
	return_num = 0
	for ch in input_str:
		return_num += ord(ch)

	return return_num
