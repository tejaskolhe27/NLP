from flask import Flask,redirect, url_for,render_template
app = Flask(__name__,template_folder='template')

@app.route('/')

def index():
    return render_template('helloworld.html')

if __name__ == '__main__':
    app.run(debug=True)    