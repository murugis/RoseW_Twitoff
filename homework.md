# Assignment 1

from flask import Flask
from.db_model import DB, User,Tweet


def create_app():
    '''create and configure instance of our Flask application.'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/parent/Desktop/RoseW_Twitoff/twitoff.sqlite3'
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
    DB.init_app(app)#link flask app to SQLAchemy

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'

    @app.route('/<username>/<followers>')
    def add_user(username,followers):
        user = User(username=username, followers=followers)
        DB.session.add(user)
        DB.session.commit()

        return f'{username} has been added to the DB!'

    
    @app.route('/<user_id>/<tweet>')
    def add_tweet(user_id,tweet):
        tweet = Tweet(user_id=user_id, tweet=tweet)
        DB.session.add(tweet)
        DB.session.commit()

        return f'{tweet} has been added to the DB!'

    return app