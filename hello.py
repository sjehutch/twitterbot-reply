#!/usr/bin/env python
import tweepy
import logging
import time
import sys
import requests
import os
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
twt = api.search(q="Fitness" , count=1 , lang="en" , result_type="recent")

#list of specific strings we want to check for in Tweets

t = ['Fitness',
	'Fitness!',
	'Fitness!!!',
	'Fitness!!',
	'fitness!',
	'fitness!!']






for s in twt:
			sn = s.user.screen_name
			m = "@%s Hello Great Tweet on fitness" % (sn)
			pic = api.media_upload('photo.jpg')
			s = api.update_status(m, s.id , media_ids = [pic.media_id_string])
			time.sleep(20)
print ("All done!")
