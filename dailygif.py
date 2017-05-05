# Name: dailygif.py
# Purpose: Sends a random gif to a friend
# Author: Robin Goyal
# Last Modified: May 5, 2017
# Usage: ./python dailygif.py
#         Pass some input when asked for 

# Giphy API: https://github.com/Giphy/GiphyAPI

import fbchat
import getpass
import urllib
import simplejson as json
import sys
import os

# Gif topic to search for
gifTopic = raw_input("Enter gif to search for: ").split()

# API call link parameters
api = "http://api.giphy.com/v1/gifs/random"
apiKey = "?api_key=dc6zaTOxFJmzC"
gifQuery = "&tag=" + "+".join(gifTopic)

# Concactenate formatted url for gif search
apiURL = api + apiKey + gifQuery

response = urllib.urlopen(apiURL)
data = json.load(response)

# Extract gif image link
gifURL = data['data']['image_original_url']

# Retrieve user information
userid = raw_input("Enter facebook username: ")
password = getpass.getpass("Password: ")

# Create facebook chat client
client = fbchat.Client(userid, password, debug = False)

# Retreive user id for friend
# Could check for correct friend and option to send to multiple friends but lazy
friendName = raw_input("FRIEND NAME: ")
friend = client.getUsers(friendName)[0].uid

# Send gif image link to friend
client.sendRemoteImage(friend, message = "", image = gifURL)