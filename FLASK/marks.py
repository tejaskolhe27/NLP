from flask import Flask,redirect, url_for,render_template
app = Flask(__name__,template_folder='template')

@app.route('/')

def result():
    data = {'physices'  : 67,'chemistry' : 78,'math' : 59}
    return render_template('result.html',result=data)

if __name__ == '__main__':
    app.run(debug=True)    