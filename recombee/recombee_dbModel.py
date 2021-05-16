from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *
import random

client = RecombeeClient('moodsic-dev', 'Pb4MhOK6751HmdEGmvISdFJqXjLDWEtVkyb2AIY4Cn1EL3vQWy9V0B236OGEj8iy')
#########################################
# WARNING Recombee API creates some problems when you're trying to add an object
# when it already exists, therefore if you want to build the model of the database, you have to 
# erase the whole database first, this is the best way yet
# adendum: requst should be done in certain order
#
# PrimaryKey means that we will transfer PrimaryKeys from our server database to the recombee database as id-s
##########################################



#DATA  MODELS FOR USERS AND MUSIC

client.send(AddUserProperty("username", "string"))
client.send(AddUserProperty("usualMood", "string"))
client.send(AddUserProperty("age", "int"))



#this can be good enough for our needs
client.send(AddItemProperty("mood", "string"))
client.send(AddItemProperty("length", "double"))
client.send(AddItemProperty("title", "string"))
client.send(AddItemProperty("viewCount" , "int"))
client.send(AddItemProperty("likeDislikeRatio", "double"))
client.send(AddItemProperty("url", "string"))



#feed firt iteration of data for testing purposes
client.send(SetUserValues("PrimaryKey1",
                         {"username" : "nika",
                          "usualMood" : "sad",
                          "age"       : 22,
                             }, cascade_create = True))


#we must loop through our datatabase of songs
#I don't know how to format string in python
#therefore I can't put link here yet
client.send(SetItemValues('PrimaryKey1',
            {"mood" : "happy",
            "length" : 3.21,
            "viewCount" : 20333,
            "likeDislikeRatio" : 1.0,
            "title" : "aurum - gold",
            "url"   : "jojosomewhatbizzare"},
            cascade_create=True))

client.send(SetItemValues('PrimaryKey2',
            {"mood" : "sad",
            "length" : 3.44,
            "viewCount" : 5000,
            "likeDislikeRatio" : 0.04,
            "title" : "too sad - I'm sad",
            "url"   : "jojoverybizzare"},
            cascade_create=True))

client.send(SetItemValues('PrimaryKey3',
            {"mood" : "chill",
            "length" : 3.11,
            "viewCount" : 100000,
            "likeDislikeRatio" : 0.9,
            "title" : "wave - relax",
            "url"   : "jojonotbizzare"},
            cascade_create=True))

client.send(SetItemValues('PrimaryKey4',
            {"mood" : "trippy",
            "length" : 2.10,
            "viewCount" : 5000000,
            "likeDislikeRatio" : 0.4,
            "title" : "blue royd - another bit in the ram",
            "url"   : "pardonmypervertsoul69"},
            cascade_create=True))

