import tweepy
import logging
import time
from config import TWEET__CONSUMER_API_KEY
from config import TWEET__CONSUMER_API_SECRET
from config import TWEET__ACCESS_TOKEN
from config import TWEET__ACCESS_TOKEN_SECRET



def create_api():
    logger = logging.getLogger()

    auth = tweepy.OAuthHandler(TWEET__CONSUMER_API_KEY, TWEET__CONSUMER_API_SECRET)
    auth.set_access_token(TWEET__ACCESS_TOKEN, TWEET__ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e

    logger.info("API created")
    return api