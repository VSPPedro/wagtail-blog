from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(o=mhc4_jv!aw-vrqz$v!skz3efj26-umcy2@dkkjf02sb06@c'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['wagtail-blog-pvspaiva.c9users.io']

try:
    from .local import *
except ImportError:
    pass
