from flask import Flask
app = Flask(__name__)

@app.route('/well')
def welcome():
    return '<h1>Welcome</h1>'

@app.route('/good')
def good():
    return '<h1>Good Bye All</h1>'

@app.route('/')
def home():
    return '<h1>You are at the home page</h1>'

if __name__ == '__main__':
    app.run(debug=True)