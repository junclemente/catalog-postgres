"""
This is the configuration file for the site and should be uploaded separately.
For security purposes, the actual file should not be posted publicly,
such as github.

Make a copy of this file and name it 'config.py'.
Then, change all the parameters below to the proper values.

"""

# Change SECRET_KEY to better password for production
SECRET_KEY = "this is a secretkey that no one else should know"

# Change DEBUG to false for production server
DEBUG = True

# DATABASE URI for DB server ie: postgresql://user:pwd@localhost/dbname
DATABASE_URI = "postgresql://user:password@localhost/dbname"

# OAUTH2 Client ID from Google
CLIENT_ID = "OAUTH2 Client ID"