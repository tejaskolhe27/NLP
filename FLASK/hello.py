from flask import Flask
app = Flask(__name__)

@app.route('/hello')

def hello_world():
    return("Welcome to the world!")

if __name__ == '__main__':
    app.run(debug=True)