# twitterbot-replypython


##This bot has  main use 
-1. It listens for a keyword example right now fitnes
-2. it responds to the user who tweeted it with a generic text, @symbol and image

-the tools used in this project were python3 

###You will want to import the following in your main .py file (i called mine hello.py) 

```python
import tweepy #Library for twitter writeen in python
import logging #Logging Duh
import time    #time module for the sleep function
import sys     #system for importing images to your tweet
import requests
import os
```python

**Step 1** 
Create a twitter application by going to https://apps.twitter.com > Create new 

**Step 2**
-Download this repo 

**Step 3**
-Update the keys with your keys otherwise you will be spamming with my twitter account :-)

**Step4 **
-Update and play around with the code (make sure you create a branch of your own first 

Step 5 
-save the py file run python hello.y and check out your twitter feed 


###to-dos 
-Showing how to run this as a background job 
-Pulling the keyword i want to search from a db or a place where i can update it on the fly 
-Better verbose logging 

##Sample 
-This is my bot responding with an image to a tweet about fitness 
![alt text](https://dl.dropboxusercontent.com/u/32232546/Screen%20Shot%202017-02-20%20at%206.39.24%20AM.png "")

