import tweepy
import logging
from config import create_api,get_keyword
import time
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

           
def search_keyword(api,keyword):
    logger.info(f"Searching for the keyword: {keyword}")
    
    new_search = keyword + " -filter:retweets"
    
    tweets = tweepy.Cursor(api.search_tweets,
              q=new_search,
              lang="en").items(30)

    tweets_list_lists = [[tweet.text, tweet.user.screen_name, tweet.user.location] for tweet in tweets]

    return tweets_list_lists

def list_to_df(tweets_list_lists):
    return pd.DataFrame(data=tweets_list_lists, 
                    columns=['tweet','user', "location"])
    
            
def main():
    api = create_api()
    keyword = get_keyword()
    while True:
        list_results = search_keyword(api,keyword)
        df = list_to_df(list_results)
        logger.info(df.head(20))
        logger.info("Waiting 60 seconds...")
        time.sleep(60)

if __name__ == "__main__":
    main()