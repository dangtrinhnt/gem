#! /usr/bin/python

import httplib2
from httplib import BadStatusLine
# import simplejson

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from apiclient import errors
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import SignedJwtAssertionCredentials
from oauth2client.client import AccessTokenRefreshError

import gdata.apps.emailsettings.client
import gdata.client.BadAuthentication
#~ from commons import *





# domain-wide
def create_service(service_account_pkcs12_file,\
						service_account_email, scope, user_email):
	"""Build and returns a Drive service object authorized with the service accounts
		that act on behalf of the given user.

	Args:
		user_email: The email of the user.
	Returns:
		Drive service object.
	"""
	f = file(service_account_pkcs12_file, 'rb')
	key = f.read()
	f.close()

	credentials = SignedJwtAssertionCredentials(service_account_email, key,\
						scope=scope, sub=user_email)
	print "Finish getting credentials for user %s" % user_email

	http = httplib2.Http()
	http = credentials.authorize(http)

	print "Finish authorize user %s" % user_email

	try:
		service = build('drive', 'v2', http=http)
		return service
	except AccessTokenRefreshError, error:
		print "Error when getting drive service of user %s:\n > Error: %s"\
						% (user_email, error)

	return None
	
	
	

		



