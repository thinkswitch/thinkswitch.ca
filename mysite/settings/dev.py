from .base import *



INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^b(oc9)h5(405&l6_vmrh8nh#&75uz@ek250ua6eqm9fgc5hl0'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

INTERNAL_IPS = [
    '127.0.0.1', 'localhost', '99.199.125.185', '*.thinkswitch.ca'
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
