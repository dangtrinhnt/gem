#! /usr/bin/env python

import gdata.apps.emailsettings.client
from gdata.client import BadAuthentication
from gdata.client import RequestError
import csv
import socket
if socket.gethostname() in ['trinh-pc',]: # add your hostname here
	from settings_local import *
else:
	from settings import *
import sys



def get_username_list_from_text(username_file_path):
	# username_list = []
	text_file = open(username_file_path, 'rb')
	username_list = text_file.read()
	text_file.close()
	username_list = username_list.split('\n')
	return username_list


def create_gdata_client(domain, admin_email, admin_password, appname='GEM'):
	try:
		client = gdata.apps.emailsettings.client.EmailSettingsClient(domain=domain)
		client.ClientLogin(email=admin_email, password=admin_password, source=appname)
		return client
	except BadAuthentication, e:
		print "Create GDATA Client error: %s\n" % e

	return None


def enable_imap(client, username):
	try:
		client.UpdateImap(username=username, enable=True)
	except RequestError, e:
		print "Update IMAP for user %s error: %s\n" % (username, e)
	
	
def enable_imap_all(domain, admin_email, admin_password, username_list):
	client = create_gdata_client(domain, admin_email, admin_password)
	if client:
		for username in username_list:
			print "Enabling IMAP on username %s...\n" % username
			enable_imap(client, username)
			print "Finish enabling IMAP on username %s\n" % username
	else:
		print "Cannot create gdata client\n"



if __name__ == "__main__":
	username_file_path = sys.argv[1]
	username_list = get_username_list_from_text(username_file_path)
	if username_list:
		enable_imap_all(SRC_DOMAIN, DOMAIN_ADMIN, DOMAIN_ADMIN_P, username_list)
