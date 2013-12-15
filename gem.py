#! /usr/bin/env python

import subprocess
import sys

from commons import *





def backup_emails(email, service_account_email, email_folder):
	command = [
		"python", "gyb.py",
		"--email", email,
		"--action", "backup",
		"--local-folder", email_folder,
		"--service-account", service_account_email
	]
	subprocess.call(command)

	
def restore_emails(email, service_account_email, email_folder):
	command = [
		"python", "gyb.py",
		"--email", email,
		"--action", "restore",
		"--local-folder", email_folder,
		"--service-account", service_account_email
	]
	subprocess.call(command)


def erase_backuped_emails(email_folder):
	email_folder += '/*'
	command = [
		"rm", "-rf",
		email_folder
	]
	subprocess.call(command)


def migrate_emails(src_email, dest_email, service_account_email, emails_folder):
	backup_emails(src_email, service_account_email, emails_folder)
	restore_emails(dest_email, service_account_email, emails_folder)	
	erase_backuped_emails(emails_folder)

def migrate_emails_all(emails_dict, service_account_email, emails_folder):
	for emails in emails_dict:
		migrate_emails(emails['src_email'], emails['dest_email'], service_account_email, emails_folder)



if __name__ == "__main__":
	emails_csv_path = sys.argv[1]
	emails_dict = get_dict_data_from_csv_file(emails_csv_path)
	
	if emails_dict:
		migrate_emails_all(emails_dict, SERVICE_ACCOUNT_EMAIL, EMAILS_FOLDER)
		



