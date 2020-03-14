from flask import Flask, render_template, url_for, request, redirect, make_response
from data import getPosts, createPost
from idGenerator import idGenerator
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

def getUserData():
    path = os.path.relpath('data\\userData.dat', os.path.dirname(__file__))
    userdata = open(path, 'r')
    userdata.readline()
    users = {}
    for line in userdata:
        currentLine = line.rstrip().lstrip().split(',')
        users[currentLine[0]] = {'password' : currentLine[1]}
    return users


def addNewUser(username, password):
    path = os.path.relpath('data\\userData.dat', os.path.dirname(__file__))
    userdata = open(path, 'a')
    userID = idGenerator()
    userdata.write(f'{username},{password},{userID}\n')
    userdata.close()

@app.route('/')
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/verification', methods=['POST'])
def verification():
    userdata = getUserData()
    user = request.form['username']
    password = request.form['password']
    if (user in userdata):
        if (password == userdata[user]['password']):
            #TODO MAKE COOKIE HERE
            response = make_response(redirect(url_for('mainScreen', username=user)))
            return response
    return redirect('login')

@app.route('/<username>/home', methods=['GET'])
def mainScreen(username):
    posts = getPosts()
    return render_template('home.html', username=username, posts=posts)

@app.route('/<username>/newpost', methods=['GET'])
def newPost(username):
    return render_template('newPost.html', username=username)

@app.route('/<username>/createpost', methods=['POST'])
def createpost(username):
    content = request.form['post_input']
    title = request.form['title']
    author = 'Henrik'
    date = '14.03.2020'
    createPost(author, date, title, content)
    return redirect(url_for('mainScreen', username=username))


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, threaded=True)