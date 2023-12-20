from flask import Flask, redirect, request, url_for
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return '<h1>Welcome %s</h1>'% name

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))

if __name__  == '__main__':
    app.run(debug=True)