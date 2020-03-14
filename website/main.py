from flask import Flask, render_template


posts = [
    {
        'title' : 'Welcome',
        'author' : 'Henrik Andreas',
        'date' : '16.12.2019',
        'content' : 'Welcome to my webpage, which is full of bullshit. On the playground you might be able to have some fun'
    }
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainScreen():
    return render_template('home.html', post=posts)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, threaded=True)