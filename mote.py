# Import for twitter
from twython import Twython
from time import sleep
from mote import Mote
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

# Mote config
mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)


def motered():
    mote.clear()
    # Sets so all channels get changed
    for channel in range(1, 2):
        # Sets all pixels to change colour
        for pixel in range(16):
            mote.set_pixel(channel, pixel, 255, 0, 0)
    mote.show()


def moteblue():
    mote.clear()
    # Sets so all channels get changed
    for channel in range(1, 2):
        # Sets all pixels to change colour
        for pixel in range(16):
            mote.set_pixel(channel, pixel, 0, 0, 255)
    mote.show()

def motegreen():
    mote.clear()
    # Sets so all channels get changed
    for channel in range(1, 2):
        # Sets all pixels to change colour
        for pixel in range(16):
            mote.set_pixel(channel, pixel, 0, 255, 0)
    mote.show()

def retrieve():
    # https://dev.twitter.com/rest/reference/get/search/tweets
    # by setting q='****' you can search for tweets to specified account*
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
        motered()
    elif '#bluekeyboard' in lookup:
        print('turn blue')
        moteblue()
    elif '#greenkeyboard' in lookup:
        print('turn green')
        motegreen()
    else:
        print('No Colour specified')
    sleep(60)

