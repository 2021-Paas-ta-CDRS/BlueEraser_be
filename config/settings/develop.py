from .base import *

import dj_database_url

DEBUG = True
DATABASES['default'] = dj_database_url.parse(get_secret('DATABASE_URL'))
