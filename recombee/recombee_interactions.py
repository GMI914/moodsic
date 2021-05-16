
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *


#############
# This file describes the types of interactions
# and how they can be used in our application
#############


# Interaction : Purchase
# it is common to send purchase interaction when user views more than 90%
# of the video
client.send(AddPurchase("PrimaryKey1", "PrimaryKey1", cascade_create = None, amount = 1,recomm_id = DEFAULT))

# Interaction : View Portions
# if we want to specify what part of the video the user watched more specifically, we can use View Portions
# for example when user views half of the video
client.send(SetViewPortion("PrimaryKey1", "PrimaryKey2", portion = 0.5, session_id = DEFAULT, cascade_create = None ))

# these two are self explanatory, more the music is watched, more it gets recommended

# Interaction : Ratings
# Ratings are in [-1, 1] where -1.0 means the worst rating possible , 0.0 neutral and 1.0 the best.
client.send(AddRating("PrimaryKey1", "PrimaryKey3", rating = 0.6, cascade_create = None))

# This should be used to rate weather it fits the mood or not and if the musics quality is good


#Don’t forget to provide the recommId parameter if the interaction is based on the recommendations. 
#It will give you very precise insight into the success of the recommendations in the Admin UI

# When users start sending bad ratings to the music, what we can do is to some time later, we should
# grab all the badly rated music and change it's mood or check the quality, therefore we need additional system 
# that will do that, different from the recommendation system


