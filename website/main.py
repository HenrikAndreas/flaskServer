from flask import Flask, render_template, url_for, request, redirect
from data import getPosts, createPost
from idGenerator import idGenerator
import os

app = Flask(__name__)

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
    username = request.form['username']
    password = request.form['password']
    if (username in userdata):
        if (password == userdata[username]['password']):
            return redirect('home')
    return redirect('login')

@app.route('/home', methods=['GET'])
def mainScreen():
    posts = getPosts()
    return render_template('home.html', posts=posts)

@app.route('/newpost', methods=['GET'])
def newPost():
    return render_template('newPost.html')

@app.route('/createpost', methods=['POST'])
def createpost():
    content = request.form['post_input']
    title = request.form['title']
    author = 'Henrik'
    date = '14.03.2020'
    createPost(author, date, title, content)
    return redirect('home')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, threaded=True)