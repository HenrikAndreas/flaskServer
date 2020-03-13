from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainScreen():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, threaded=True)