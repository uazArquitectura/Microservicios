# -*- coding: utf-8 -*-

import sqlite3


class PersistenciaTweets:
    def __init__(self):
        self.open_connection()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS tweets(
                user_name TEXT,
                tweet_hashtag TEXT,
                tweet_body TEXT,
                tweet_date DATETIME,
                PRIMARY KEY (user_name, tweet_date)
            )
            ''')
        self.conn.commit()
        self.conn.close()

    def open_connection(self):
        self.conn = sqlite3.connect('tweets.db')
        self.cursor = self.conn.cursor()

    def insert_tweet(self, tweet):
        print tweet
        self.open_connection()
        self.cursor.execute(
            'INSERT OR IGNORE INTO tweets (tweet_body, tweet_date, '
            'user_name, tweet_hashtag) VALUES (?, '
            '?, ?, ?)', tweet)
        self.conn.commit()
        self.conn.close()

    def insert_tweets(self, tweets):
        self.open_connection()
        self.cursor.executemany(
            'INSERT OR IGNORE INTO tweets (tweet_body, tweet_date, '
            'user_name, tweet_hashtag) VALUES (?, '
            '?, ?, ?)', tweets)
        self.conn.commit()
        self.conn.close()

    def get_all_tweets(self):
        self.open_connection()
        tweets = self.cursor.execute('SELECT * FROM tweets').fetchall()
        self.conn.commit()
        self.conn.close()
        return tweets

    def get_tweets_by_hashtag(self, hashtag):
        self.open_connection()
        tweets = self.cursor.execute('SELECT * FROM tweets WHERE '
                                     'tweet_hashtag=?', [hashtag])
        data = tweets.fetchall()
        print self.cursor.description
        print data[0]
        self.conn.commit()
        self.conn.close()
        return [{'user_name': row[0], 'tweet_hashtag': row[1],
                 'tweet_body': row[2], 'tweet_date': row[3]} for row in data]
