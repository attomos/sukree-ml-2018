# Install dependencies and activate virtualenv

    $ pip install pipenv # if needed
    $ pipenv install
    $ pipenv shell


# How to run this

1. Create [Twitter app](https://apps.twitter.com/) to obtain credentials
2. Add these to your env vars (via command line or using PyCharm)
```
    CONSUMER_KEY = <your_consumer_key>
    CONSUMER_SECRET = <your_consumer_secret>
    ACCESS_TOKEN_KEY = <your_access_token_key>
    ACCESS_TOKEN_SECRET = <your_access_token_secret>
```
3. Run `fetch_tweets.py` (you need the above credentials) to get recent tweets from the subjects
4. Run `main.py` to perform NMF and LDA on the data


# Credit

Big thanks to this [Medium
post](https://medium.com/mlreview/topic-modeling-with-scikit-learn-e80d33668730)
which is an excellent introduction to topic modeling with Scikit Learn
