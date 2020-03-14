from flask import Flask, render_template, url_for, request, redirect



app = Flask(__name__)

@app.route('/', methods=['GET'])
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
    return redirect('home')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, threaded=True)