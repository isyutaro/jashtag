from common import *

DEBUG = True

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
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

ALLOWED_HOSTS = ["jashtag.intersys.mx"]

# Twitter Settings
TWITTER_CONSUMER_KEY = 'ph91wQSzf3BNB4fjDENtoeyhb'
TWITTER_CONSUMER_SECRET = 'Snc7doueTebGr2V8ONdy31ShRyCJnO9HmcKwbBulnwlzjBOfJk'
TWITTER_ACCESS_TOKEN = '84100110-EKAtSHAamqgoSrYWXpiA01Uh522yrsFoGuAd4CeaS'
TWITTER_TOKEN_SECRET = '5Qa7sxCdb4VRTsIgiHDK98iiarMZcYKfXd6UYcBGsYWoD'
TWITTER_HASH_TAG = 'Ally'
TWITTER_FOLLOW_USER = '84100110'
TWEETS_PER_QUERY = 15
