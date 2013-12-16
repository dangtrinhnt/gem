GEM - Google Email Migration
=============================

This project uses the [Got-Your-Back script](https://code.google.com/p/got-your-back/) as the core to help you to migrate all users's emails from old domain to the new one in Google App.


### Update


##### + 12/16/2013:

+ Use condition number
+ Use emails folder input
+ Get error users when enabling IMAP


##### + 12/15/2013:

+ Enable IMAP for all users (only need to do this on old domain)
+ Backup emails
+ Restore emails
+ Delete emails folder
+ Migrate emails of all users to new domain


### Requirements

+ gdata==2.0.18
+ google-api-python-client==1.2
+ httplib2==0.8
+ pyOpenSSL==0.13.1
+ uritemplate==0.6
+ gyb==0.20a



### Usage

##### 1/ Create a virtualenv environment and install requirements:

`username@user-host:/path/to/gem$ virtualenv /home/.venv/your_env`
`username@user-host:/path/to/gem$ source /home/.venv/your_env/bin/activate`
`(your_env)username@user-host:/path/to/gem$ pip install -r requirements.txt`

##### 2/ Enable IMAP on all user accounts (only old domain):

`(your_env)username@user-host:/path/to/gem$ ./enable_imap.py /path/to/username_list.csv`

* username_list.csv (one username per line):

| --------- |
| username1 |
| username2 |
| username3 |


##### 3/ Run the migration script to start the emails migrations:

`(your_env)username@user-host:/path/to/gem$ python gem.py /path/to/email_mapping_list.csv <condition number> /path/to/emails/folder`

* email_mapping_list.csv (2 columns: src - old domain email address, dest - new domain email address):

`src,dest
oldomain@mydomain.com,newdomain@mydomain.com`

| src                    | dest                    |
| ---------------------- | ----------------------- |
| oldomain1@mydomain.com | newdomain1@mydomain.com |
| oldomain2@mydomain.com | newdomain2@mydomain.com |
| oldomain3@mydomain.com | newdomain3@mydomain.com |


* condition number: all posible numbers are: 

`0,1,2,3,4,5,6,7,8,9 or 'all'`


### References

+ [0] [https://code.google.com/p/got-your-back/wiki/GettingStarted](https://code.google.com/p/got-your-back/wiki/GettingStarted)
+ [1] [https://developers.google.com/admin-sdk/email-settings/](https://developers.google.com/admin-sdk/email-settings/)
+ [2] [https://gdata-python-client.googlecode.com/hg/pydocs/gdata.apps.emailsettings.client.html](https://gdata-python-client.googlecode.com/hg/pydocs/gdata.apps.emailsettings.client.html)


### Contact

+ Email: dangtrinhnt[at]gmail[dot]com
+ Twitter: [@dangtrinhnt](https://twitter.com/dangtrinhnt)
