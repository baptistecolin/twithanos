import twitter
import json

credentials = json.loads(open("credentials").read())

api = twitter.Api(consumer_key=credentials["api_key"],
            consumer_secret=credentials["api_secret_key"],
            access_token_key=credentials["access_token"],
            access_token_secret=credentials["access_token_secret"])

def softblock(user_id, screen_name):
    api.CreateBlock(user_id=user_id, screen_name=screen_name)
    api.DestroyBlock(user_id=user_id, screen_name=screen_name)

