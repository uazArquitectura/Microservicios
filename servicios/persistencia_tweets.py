import sqlite3
from datetime import datetime


class ConectorSqlite:
    def __init__(self):
        self.open_connection()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS tweets(
                user_name TEXT,
                movie_title TEXT,
                tweet_body TEXT,
                tweet_date DATETIME,
                tweet_sentiment TEXT,
                PRIMARY KEY (user_name, tweet_date)
            )
            ''')
        self.conn.commit()
        self.conn.close()

    def open_connection(self):
        self.conn = sqlite3.connect('tweets.db')
        self.cursor = self.conn.cursor()

    def insert_tweet(self, tweet):
        self.open_connection()
        self.cursor.execute(
            'INSERT OR IGNORE INTO tweets VALUES (?, ?, ?, ?, ?)',
            tweet)
        self.conn.commit()
        self.conn.close()

    def get_tweets(self):
        self.open_connection()
        tweets = self.cursor.execute('SELECT * FROM tweets').fetchall()
        self.conn.commit()
        self.conn.close()
        return tweets


testConector = ConectorSqlite()
tweet = ('@porfirio', 'Stranger Things', 'Hola mundo este es mi tweet',
         str(datetime.now()), 'neg')
testConector.insert_tweet(tweet)
print testConector.get_tweets()
