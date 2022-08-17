import tweepy
import logging
from config import create_api, get_credentials
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class KeywordStreams(tweepy.Stream):
#     def __init__(self, api):
#         self.api = api
#         # self.me = api.me()
        
    
    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")

#     def on_status(self, tweet):
#         logger.info(f"Processing tweet id {tweet.id}")
#         # if tweet.in_reply_to_status_id is not None or \
#         #     tweet.user.id == self.me.id:
#         #     # This tweet is a reply or I'm its author so, ignore it
#         #     return
#         if not tweet.favorited:
#             # Mark it as Liked, since we have not done it yet
#             print(tweet.text)
#             # try:
#             #     tweet.favorite()
#             # except Exception as e:
#             #     logger.error("Error on fav", exc_info=True)
#         if not tweet.retweeted:
#             # Retweet, since we have not retweeted it yet
#             try:
#                 tweet.retweet()
#             except Exception as e:
#                 logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    consumer_key,consumer_secret,access_token,access_token_secret = get_credentials()
    tweets_listener = KeywordStreams(consumer_key,consumer_secret,access_token,access_token_secret)
    tweets_listener.sample()
    tweets_listener.filter(track=keywords, languages=["en"], stall_warnings=True)

if __name__ == "__main__":
    main(["covid"])