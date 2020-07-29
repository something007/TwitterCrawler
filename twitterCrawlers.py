import tweepy
import pandas as pd

# Bearea Token : AAAAAAAAAAAAAAAAAAAAAATPGAEAAAAAr%2FTVOHCN1KPs0M51WKAD9ZzHnv4%3D6tzmXXXCJGmKOct5jxFhxLrHEf3syI3dPIAzzah6LeAy0KtLT4

consumer_key = 'fJnRMw94tSkeHtYGuhsNGMC67'
consumer_secret = '33DhsTyu82f3cbB2KQgrwgIV7uDEQaLbGMe0z1dYLGp1AmxNvn'
access_token = '1241963014208684032-the0kiD7BHE0WmvfG5IIwU3cZsRqxP'
access_token_secret = 'aGlAKc104IXX73MDqB3ion0jhglB9LaNXOLDWAWf3soNF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


query = input("Hashtag : ")


df = pd.DataFrame(columns=["create_at","text","hashtag","retweet_count","favourite_count"])
for tweet in tweepy.Cursor(api.search,q=query,count=100,result_type="recent",tweet_mode='extended').items(10000):
    entity_hashtag = tweet.entities.get('hashtags')
    hashtag = ""
    for i in range(0,len(entity_hashtag)):
        hashtag = hashtag +"/"+entity_hashtag[i]["text"]
    re_count = tweet.retweet_count
    create_at = tweet.created_at
    try:
        text = tweet.retweeted_status.full_text
        fav_count = tweet.retweeted_status.favorite_count
    except:
        text = tweet.full_text
        fav_count = tweet.favorite_count
    new_column = pd.Series([create_at,text,hashtag,re_count,fav_count], index=df.columns)
    df = df.append(new_column,ignore_index=True)

df.to_csv("{}.csv".format(query), encoding="utf-8")

