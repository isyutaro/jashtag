from common import *

# Emails aren't send but displayed in console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jashtag_db',
        'USER': 'jashtag_usr',
        'PASSWORD': 'wE6QaTsYBidXO3J5AVQX',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ["jashtag.isyutaro.com"]

