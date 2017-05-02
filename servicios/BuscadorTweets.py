# -*- coding: utf-8 -*-

from twython import Twython
import sys
import requests.packages.urllib3

reload(sys)
requests.packages.urllib3.disable_warnings()
sys.setdefaultencoding("utf-8")


class Tweet:
    def __init__(self, screen_name, hashtag, text, created_at):
        self.screen_name = screen_name
        self.hashtag = hashtag
        self.text = text
        self.created_at = created_at


class BuscadorTweets:
    def __init__(self):
        self.ConsumerKey = "jfij525430WHSqo46VCXiTA95"
        self.ConsumerSecret = "BfFZ6iSPTj7u699apBGY3Yu4RHMLOVR61QGASVenGVLdjh6lRb"
        self.AccessToken = "3290922366-kDNgrRkVLYnVQXDTtKbJqH1wCj0fkVKJy3PotjV"
        self.AccessTokenSecret = "Ulb7EPn9VQ4rWa8wIXflzGvMuNrZ1yBtVYQ6MSTvtl1We"
        self.twitter = Twython(self.ConsumerKey, self.ConsumerSecret,
                               self.AccessToken, self.AccessTokenSecret)

    def to_hashtag(self, text):
        return '#' + ''.join(c for c in text.title() if not c.isspace())

    def search_tweets(self, title):
        search_query = '@netflix' + self.to_hashtag(title)
        result = self.twitter.search(q=search_query, count=20)
        tweets = []
        for status in result["statuses"]:
            screen_name = status["user"]['screen_name']
            hashtag = self.to_hashtag(title)
            text = status['text']
            created_at = status['created_at']
            tweets.append(Tweet(screen_name, hashtag, text, created_at)
                          .__dict__)
        return tweets
