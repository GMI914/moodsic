from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *

# By the Definition :

# Scenario defines a particular application of recommendations at your website, your mobile app or emailing campaign. #
# It can be for example homepage, watch-next, cart or emailing-after-purchase. #

# We can define different scenarios, with different logic for our website
# But we can control that with API requests, I don't know which one is better yet

# I think we can use Filtering and Boosting with API using Recombees Query Language
# If we implement that we can tell too choose music with less views ... 

# At this point I don't know how to use send queries with API , maybe there's no way to do it
# therefore I will do it in UI




# Business Rules #

# Rule 1 #

# Prioritize music with less viewcount and maybe in contrast with prioritizing more newly uploaded music

# if'viewCount' in [0, 9999] then 4 else if 'viewCount' in [10000, 999999] then 3 else if [ 1000000, 50000000] then 2 else 1

# Rule 2 #

# Prioritize music with higher like/dislike ratio / simple but works

# if 'likeDislikeRatio' > 0.5 then 2 else 1

# Rule 3 #

# Maybe prioritize music with smaller runtime 