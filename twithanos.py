import twitter
import json
import random

credentials = json.loads(open("credentials").read())

#api = twitter.Api(consumer_key=credentials["api_key"],
#            consumer_secret=credentials["api_secret_key"],
#            access_token_key=credentials["access_token"],
#            access_token_secret=credentials["access_token_secret"])

def softblock(user_id, screen_name):
    api.CreateBlock(user_id=user_id, screen_name=screen_name)
    api.DestroyBlock(user_id=user_id, screen_name=screen_name)

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def dedup(l):
  res = [ ]
  for elem in l:
    if elem not in res:
      res.append(elem)

  return res

def inter(l1, l2):
  res = []
  for x1 in l1:
    if x1 in l2:
      res.append(x1)

  for x2 in l2:
    if x2 in l1 and x2 not in res:
      res.append(x2)

  return res

def exclude(l1, l2):
  res = []
  for elem in l1:
    if elem not in l2:
      res.append(elem)

  return res

def filter_out_indexes(l, idxs):
  print("list : " + str(l))
  print("idxs : " + str(idxs))
  res = []
  for i in range(len(l)):
    if str(i) not in idxs:
      print(str(i) + " is not in " + str(idxs))
      res.append(l[i])
  return res

followers = api.GetFollowers()

#followers = [
#              {'name': 'someone i luv <3',            'screen_name': 'myFrienD99' },
#              {'name': 'relou1',                      'screen_name': 'relou1' },
#              {'name': 'relou2',                      'screen_name': 'relou2' },
#              {'name': 'relou3',                      'screen_name': 'relou3' },
#              {'name': 'relou4',                      'screen_name': 'relou4' },
#              {'name': 'relou5',                      'screen_name': 'relou5' },
#            ]

followings = api.GetFriends()
#followings = [
#              {'name': 'someone i luv <3',            'screen_name': 'myFrienD99' },
#              {'name': 'monkey',                      'screen_name': 'crevicedwelling' },
#              {'name': 'Arnaud Montebourg',           'screen_name': 'Montebourg' },
#            ]


mutuals = inter(followers, followings)
non_mutuals = exclude(followers, followings)
print (f"{len(followers)} followers")
print (f"{len(followings)} followings")
print (f"{len(mutuals)} mutuals")

nb = 0
confirmed=False
while not confirmed:
  percentage = input("What percentage of your followers do you want to get rid of ? ")
  if (is_number(percentage)):
    nb = min(int(len(followers)*float(percentage)*0.01), len(followers) - len(mutuals))
    letsgo=input(f"{nb} followers will be softblocked. Is that ok ? (type \"y\" if yes) ")
    if (letsgo == "y"):
      confirmed=True
  else:
    print("Not a valid percentage")

assert (len(non_mutuals) == len(followers) - len (mutuals))
print ("computing list of people who will get softblocked ...")

print(str(nb) + " people will be softblocked")

to_block = random.sample(non_mutuals, nb)

sparing_over = False
while not sparing_over:

  print("List of people who will get blocked : ")
  for i in range(len(to_block)):
      user = to_block[i]
      print(f"{i} : {user.name}           (@{user.screen_name})")
#      print(f"{i} : {user['name']}           (@{user['screen_name']})")

  sparing_decision=False
  spare_picking = False
  while not sparing_decision:
    to_spare_or_not_to_spare = input("Is there one or several person you'd like to spare ? (y/n) ")
    sparing_decision=True
    if (to_spare_or_not_to_spare == "y"):
      spare_picking = True
    elif (to_spare_or_not_to_spare == "n"):
      spare_picking = False
      sparing_over=True
    else:
      sparing_decision = False

  if spare_picking :
    correct_input = False
    lucky_ones_list = []
    while not correct_input:
      lucky_ones = input("Enter the indices of the lucky account(s) you'd like to spare. (space-separated list of integers) \n")
      correct_input = True
      for s in lucky_ones.split(" "):
        if not str.isdigit(s):
          correct_input = False
          break
      if correct_input:
        lucky_ones_list = lucky_ones.split(" ")

    to_block = filter_out_indexes(to_block, lucky_ones_list)


ready = input("Do you confirm you want to perform the mass softblock ? type \"y\" if yes : ")
if ready == "y" :
    print("starting thanos-blocking ...")
    for user in to_block:
        print("soft-blocking user " + user.name + "; ID : " + str(user.id))
        softblock(user.id, user.name)

    print ("Done !")
else:
    print("No softblock performed")

