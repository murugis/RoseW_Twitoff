from os import getenv
from flask import Flask,render_template,request#knows how to read the html file
from .db_model import DB, User
from .twitter import add_user_tweepy,update_all_users
from .predict import predict_user


def create_app():
    '''create and configure instance of our Flask application.'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/parent/Desktop/RoseW_Twitoff/twitoff.sqlite3'
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
    DB.init_app(app)#link flask app to SQLAchemy

    @app.route('/')
    def root():
        return render_template('base.html',title='Home', users=User.query.all())

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])

    def add_or_update_user(name=None, message=''):
        name = name or request.values['user_name']

        try:
            if request.method == "POST":
                add_user_tweepy(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.username == name).one().tweet
        except Exception  as e:
            print(f'Error adding {name}: {e}')
            tweets = []
        
        return render_template('user.html',title=name, tweets=tweets, message=message)
    
    @app.route("/compare", methods=['POST'])
    def compare(message=''):
        user1 = request.values['user1']
        user2 = request.values['user2']
        tweet_text = request.values['tweet_text']

        if user1 == user2:
            message = "Cannot compare a user to themselves"
        else:
            prediction = predict_user(user1,user2,tweet_text)

            message = f'''{tweet_text} is more likely to be said by {user1 if prediction else user2} 
                          than {user2 if prediction else user1}'''


        return render_template('predict.html', title='Prediction', message=message)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset Database!', users=User.query.all())
    
    @app.route('/update', methods=['GET'])
    def update():
        update_all_users()
        return render_template('base.html', title='All Tweets Updated',users=User.query.all())
    
    #@app.route('/<user_id>/<tweet>')
    #def add_tweet(user_id,tweet):
        #tweet = Tweet(user_id=user_id, tweet=tweet)
        #DB.session.add(tweet)
        #DB.session.commit()

        #return f'{tweet} has been added to the DB!'

    return app
