#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/jateng/")

from jateng import app as application
application.secret_key = 'ini secret key'
