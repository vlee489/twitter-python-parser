# Import for twitter
from twython import Twython
import time
from mote import Mote
from colorsys import hsv_to_rgb
# Imports auth keys from auth.py
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

# ====================================
# This is the Mote config setting and the definitions
# for the colour changing.

# Mote config
mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)


# Used defines the 0-255 colour of red, green, blue
def motecolour(red, green, blue):
    mote.clear()
    # Sets so all channels get changed
    for channel in range(1, 5):
        # Sets all pixels to change colour
        for pixel in range(16):
            # sets colour
            mote.set_pixel(channel, pixel, red, green, blue)
    mote.show()


# RAINBOW
def moterainbow():
    h = 1
    timeout = time.time() + 60
    while True:
        for channel in range(1, 5):
            pixel_count = mote.get_pixel_count(channel)
            for pixel in range(pixel_count):
                hue = (h + ((channel - 1) * pixel_count * 5) + (pixel * 5)) % 360
                r, g, b = [int(c * 255) for c in hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
                mote.set_pixel(channel, pixel, r, g, b)
        mote.show()
        time.sleep(0.05)
        if time.time() > timeout:
            break
# ====================================


# ====================================
# This is responsible for retrieving the last tweet
# on Twitter (dependent of search query)
def retrieve():
    # https://dev.twitter.com/rest/reference/get/search/tweets
    # by setting q='****' you can search for tweets to specified account
    # count specifies how many status updates you want returned, in our case 1
    search = twitter.search(q='@vlee888', count=1)
    # used to look into dictionary
    tweets = search['statuses']
    for tweet in tweets:
        status = tweet['text']
        return status
# ====================================

while True:
    lookup = retrieve()
    print(lookup)
    # the status contains '****' then run bellow
    if '#redkeyboard' in lookup:
        print('turn red')
        motecolour(255, 0, 0)
        time.sleep(60)
    elif '#bluekeyboard' in lookup:
        print('turn blue')
        motecolour(0, 0, 255)
        time.sleep(60)
    elif '#greenkeyboard' in lookup:
        print('turn green')
        motecolour(0, 255, 0)
        time.sleep(60)
    elif '#keyboardrainbow' in lookup:
        print('RAINBOW Time!')
        moterainbow()
    else:
        print('No Colour specified')
        time.sleep(10)
