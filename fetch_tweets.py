import csv
import pathlib

import os
import twitter

from common import ACCOUNTS

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN_KEY = os.environ.get('ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)


def get_tweets(screen_name, cls):
    print('Getting tweets from {} ({})'.format(screen_name, cls))
    statuses = api.GetUserTimeline(screen_name=screen_name, count=200)
    return [(s.text, cls) for s in statuses]


if __name__ == '__main__':
    pathlib.Path('data').mkdir(parents=True, exist_ok=True)
    for cls, screen_names in ACCOUNTS.items():
        for screen_name in screen_names:
            tweets = get_tweets(screen_name, cls)
            with open('data/{}_{}.csv'.format(cls, screen_name), 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                                    dialect=csv.excel)
                writer.writerows(tweets)
