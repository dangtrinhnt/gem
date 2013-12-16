#! /usr/bin/env python

import subprocess
import sys
import socket
if socket.gethostname() in ['trinh-pc', 'SRVR-UMailMigration',]: # add your hostname here
	from settings_local import *
else:
	from settings import *
from commons import *
import os






def backup_emails(email, service_account_email, email_folder):
	command = [
		"python", "gyb.py",
		"--email", email,
		"--action", "backup",
		"--local-folder", email_folder,
		"--service-account", service_account_email
	]
	print "Executing commnad: %s" % command
	subprocess.call(command)

	
def restore_emails(email, service_account_email, email_folder):
	command = [
		"python", "gyb.py",
		"--email", email,
		"--action", "restore",
		"--local-folder", email_folder,
		"--service-account", service_account_email
	]
	print "Executing commnad: %s" % command
	subprocess.call(command)


def erase_backuped_emails(email_folder):
	email_folder += '/*'
	command = 'rm -rf %s' % email_folder
	print "Executing commnad: %s" % command
	subprocess.call(command, shell=True)


def migrate_emails(src_email, dest_email, service_account_email, email_folder):
	backup_emails(src_email, service_account_email, email_folder)
	restore_emails(dest_email, service_account_email, email_folder)	
	erase_backuped_emails(email_folder)


def migrate_emails_all(emails_dict, service_account_email, email_folder, condition_number):
	
	for emails in emails_dict:
		num = str_to_num(emails['src']) % 10
		if num in condition_number or condition_number[0]==-1:
			migrate_emails(emails['src'], emails['dest'], service_account_email, email_folder)



if __name__ == "__main__":
	emails_csv_path = sys.argv[1]
	#~ print type(emails_csv_path)
	emails_dict = get_dict_data_from_csv_file(emails_csv_path)
	if sys.argv[2] == 'all':
		condition_number = [-1]
	else:
		condition_number = map(int, sys.argv[2].split(','))

	if emails_dict:
		migrate_emails_all(emails_dict, SERVICE_ACCOUNT_EMAIL, EMAILS_FOLDER, condition_number)
		



