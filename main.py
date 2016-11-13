# Import for twitter
from twython import Twython
from time import sleep
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Auth With twitter
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


def retrieve():
    # https://dev.twitter.com/rest/reference/get/search/tweets
    # by setting q='****' you can search for tweets to specified account
    search = twitter.search(q='@vlee888', count=1)
    # used to look into dictionary
    tweets = search['statuses']
    for tweet in tweets:
        status = tweet['text']
        return status

while True:
    lookup = retrieve()
    print(lookup)
    # the status contains '****' then run bellow
    if '#redkeyboard' in lookup:
        print('turn red')
    elif '#bluekeyboard' in lookup:
        print('turn blue')
    elif '#greenkeyboard' in lookup:
        print('turn green')
    else:
        print('No Colour specified')
    sleep(60)

