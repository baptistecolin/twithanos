import twitter
import json
import random

credentials = json.loads(open("credentials").read())

api = twitter.Api(consumer_key=credentials["api_key"],
            consumer_secret=credentials["api_secret_key"],
            access_token_key=credentials["access_token"],
            access_token_secret=credentials["access_token_secret"])

def softblock(user_id, screen_name):
    api.CreateBlock(user_id=user_id, screen_name=screen_name)
    api.DestroyBlock(user_id=user_id, screen_name=screen_name)

sgt_bot_id = 867280041339744257
sgt_bot_name = "singletau_bot"

followers = api.GetFollowers()
followings = api.GetFriends()

#followers  = [ "a", "b", "c", "d", "e", "f", "g" ]
#followings = [ "a", "b", "r", "t", "u", "w", "x", "y", "z" ]

print(str(len(followers)) + " followers")
print(str(len(followings)) + " followings")

mutuals = list(set(followers) & set(followings))

print (str(len(mutuals)) + " mutuals")

non_mutuals = list(set(followers) - set(mutuals))

assert (len(non_mutuals) == len(followers) - len (mutuals))

print ("computing list of people who will get blocked ...")

nb = min(int(len(followers)/2), len(followers) - len(mutuals))

print(str(nb) + " people will be blocked")

to_block = random.sample(non_mutuals, nb)

print("List of people who will get blocked : ")
for user in to_block :
    print(user.name)

ready = input("Do you confirm you want to perform the mass block ? type \"y\" if yes : ")
if ready == "y" :
    print("starting thanos-blocking ...")
    for user in to_block:
        print("soft-blocking user " + user.name + "; ID : " + str(user.id))
        softblock(user.id, user.name)

print ("Done !")
#output = softblock(sgt_bot_id, sgt_bot_name)
#print(output)

