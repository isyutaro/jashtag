# coding: utf-8
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from django.conf import settings
from django.core.management.base import BaseCommand

class TwitterStreamListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        a = json.loads(data)
        print "user: ", a['user']['screen_name']
        print a['text']
        print '-----------------------------'
        return True

    def on_error(self, status):
        print(status)


class Command(BaseCommand):
    help = "Streams Twitter"
    def handle(self, **options):
        auth = OAuthHandler(
            settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET
        )
        auth.set_access_token(
            settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_TOKEN_SECRET
        )
        print '[-] Auth set'
        stream = Stream(
            auth=auth, listener=TwitterStreamListener()
        )
        print '[-] Init stream: {}'.format(settings.TWITTER_HASH_TAG)
        # stream.filter(follow=[settings.TWITTER_FOLLOW_USER])
        # When whe want to stream a hashtag use filter instade of userstream
        # stream.filter(track=[settings.TWITTER_HASH_TAG])
        stream.filter(track=[settings.TWITTER_HASH_TAG])

