#!/usr/bin/env python
import tweepy
import logging
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
twt = api.search(q="Fitness")

#list of specific strings we want to check for in Tweets

t = ['Fitness',
	'Fitness!',
	'Fitness!!!',
	'Fitness!!',
	'fitness!',
	'fitness!!']

for s in twt:
			sn = s.user.screen_name
			m = "@%s Hello Great Tweet" % (sn)
			s = api.update_status(m, s.id)
print ("All done!")
