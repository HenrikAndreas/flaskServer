from flask import Flask, render_template
from data import getPosts



app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainScreen():
    posts = getPosts()
    return render_template('home.html', posts=posts)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, threaded=True)