from flask import render_template, request
from twitoff_app import app, DB
from .models import User
from .twitter import add_or_update_user
from .predict import predict_user


# route determines location
@app.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', title='Home', users=users)


@app.route('/user', methods=['POST'])
@app.route('/user/<name>', methods=['GET'])
def user(name=None):
    message = ''
    name = name or request.values['user_name']
    try:
        if request.method == 'POST':
            add_or_update_user(name)
            message = f'User {name} successfully added!'
        tweets = User.query.filter(User.name == name).one().tweets
    except Exception as e:
        message = f'Error adding {name}: {e}'
        tweets = []
    return render_template('user.html', title=f'{name}', tweets=tweets,
                           message=message)


@app.route("/about")
def about():
    users = User.query.all()
    return render_template('about.html', title='About', users=users)


@app.route('/reset')
def reset():
    DB.drop_all()
    DB.create_all()
    return render_template('home.html', title='Reset', users=[])


@app.route('/predict', methods=['POST'])
def predict():
    user1 = request.values['user1']
    user2 = request.values['user2']
    tweet_text = request.values['tweet_text']
    users = User.query.all()
    usernames = [user.name for user in users]
    if user1 not in usernames:
        raise ValueError('User 1 is not in the app. Please add user first')
    elif user2 not in usernames:
        raise ValueError('User 2 is not in the app. Please add user first')
    else:
        pred = predict_user(user1, user2, tweet_text)[0]
        message = message = ' is more likely to tweet this than '
        if pred == 0:
            winner = user2
            loser = user1
        else:
            winner = user1
            loser = user2
        return render_template('predict.html', title='Prediction',
                               winner=winner, loser=loser, message=message)
