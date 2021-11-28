from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.friendship import Friendship
from flask_app.models.user import User

@app.route('/')
def start():
    return redirect('/friendships')

@app.route('/friendships')
def friendships():
    friendships = Friendship.get_all()
    users = User.get_all()
    return render_template('friendships.html', friendships=friendships, users=users)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name']
    }
    User.create(data)
    return redirect('/friendships')

@app.route('/create_friendship', methods=['POST'])
def create_friendship():
    data = {
        'user_id' : request.form['user'],
        'friend_id' : request.form['friend']
    }
    if Friendship.check(data) == True:
        return redirect('/friendships')
    Friendship.create(data)
    return redirect('/friendships')