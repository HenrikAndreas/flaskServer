from flask import Flask, render_template, url_for, request, redirect


posts = [
    {
        'title' : 'Welcome',
        'author' : 'Henrik Andreas',
        'date' : '16.12.2019',
        'content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
   {
        'title' : 'Great title',
        'author' : 'Henrik Andreas',
        'date' : '16.12.2019',
        'content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    }
    
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def mainScreen():
    return render_template('home.html', posts=posts)

@app.route('/newpost', methods=['GET'])
def newPost():
    return render_template('newPost.html')

@app.route('/createpost', methods=['POST'])
def createpost():
    content = request.form['post_input']
    title = request.form['title'] 
    return redirect('home')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, threaded=True)