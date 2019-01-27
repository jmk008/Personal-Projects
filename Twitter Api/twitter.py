from twython import Twython #Python Library for twitter
from twython import TwythonStreamer
import random

#Authentication keys
from auth import (
    consumer_key,
    comsumer_key_secret,
    access_token,
    access_token_secret
)


twitter = Twython(
    consumer_key,
    comsumer_key_secret,
    access_token,
    access_token_secret
)

#Sending a random tweet on Twitter
choices = ['New Fav Song: Whats up danger', 'Gooo Patriots!!', 'Crush Rams']
message = random.choice(choices)
twitter.update_status(status=message)
print("Tweeted: %s" % message)


#Uploading an image on Twitter
message = "Hello World - here's a picture!"
image = open('image.jpg', 'rb') #image path
response = twitter.upload_media(media=image) #getting the media id from twitter
media_id = [response['media_id']]
twitter.update_status(status=message, media_ids=media_id) #uploading the image
print("Tweeted: " + message)


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print("@{}:{}".format(username, tweet))


stream = MyStreamer(
    consumer_key,
    comsumer_key_secret,
    access_token,
    access_token_secret
)

#Tracking tweets with the key word "raspberry pi"
stream.statuses.filter(track='raspberry pi')