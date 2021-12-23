import os
from distutils.util import strtobool

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
	SECRET_KEY = "SECRET_KEY"

DEBUG = os.environ.get("DEBUG")
if not DEBUG:
	DEBUG = "true"

DEBUG = strtobool(DEBUG)
