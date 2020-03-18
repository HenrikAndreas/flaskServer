from flask import Flask, render_template, url_for, request, redirect, make_response, session
from data import getPosts, createPost, addNewUser, getUserData
from idGenerator import idGenerator
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

@app.route('/')
@app.route('/login', methods=['GET'])
def login():
    try:
        passwordValidator = session['passwordValidator']
        usernameValidator = session['usernameValidator']
        return render_template('login.html', userValidator=usernameValidator,
            passwrdValidator=passwordValidator)
    except:
        return render_template('login.html')


@app.route('/verification', methods=['POST'])
def verification():
    userdata = getUserData()
    user = request.form['username']
    password = request.form['password']
    if (user in userdata):
        if (password == userdata[user]['password']):
            if ('usernameValidator' in session):
                session.pop('usernameValidator')
            if ('passwordValidator' in session):
                session.pop('passwordValidator')
            
            response = make_response(redirect(url_for('mainScreen', username=user)))
            response.set_cookie('id', userdata[user]['id'])
            return response
        else:
            session['usernameValidator'] = True
            session['passwordValidator'] = False
            return redirect(url_for('login'))

    session['usernameValidator'] = False
    session['passwordValidator'] = False
    return redirect(url_for('login'))

@app.route('/registration', methods=['GET'])
def registration():
    try:
        usernameValidator = session['usernameExists']
        passwordValidator = session['passwordValid']
        return render_template('registration.html', userExists=usernameValidator,
            passwordValid=passwordValidator)
    except:
        return render_template('registration.html')

@app.route('/register-verification', methods=['POST'])
def registerVerification():
    userdata = getUserData()
    username = request.form['username']
    password = request.form['password']
    confPassword = request.form['conf_password']
    if (username in userdata):
        session['usernameExists'] = True
        session['passwordValid'] = None
        return redirect(url_for('registration'))
    else:
        if (password != confPassword):
            session['usernameExists'] = False
            session['passwordValid'] = False
            return redirect(url_for('registration'))

        else:
            session['usernameExists'] = False
            session['passwordValid'] = True
            addNewUser(username, password)

    return redirect(url_for('login'))

@app.route('/<username>/home', methods=['GET'])
def mainScreen(username):
    userdata = getUserData();
    idCookie = request.cookies.get('id')
    if (idCookie == userdata[username]['id']):
        posts = getPosts()
        return render_template('home.html', username=username, posts=posts)
        
    return "Access denied"
    

@app.route('/<username>/newpost', methods=['GET'])
def newPost(username):
    userdata = getUserData();
    idCookie = request.cookies.get('id')
    if (idCookie == userdata[username]['id']):
        return render_template('newPost.html', username=username)

    return "Access denied"

@app.route('/<username>/createpost', methods=['POST'])
def createpost(username):
    content = request.form['post_input']
    title = request.form['title']
    author = username
    createPost(author, title, content)
    return redirect(url_for('mainScreen', username=username))


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, threaded=True)