from flask import Flask,request, url_for,render_template
app = Flask(__name__,template_folder='template')

@app.route('/')
def student():
    return render_template('fillmarks.html')

@app.route('/result',methods =['GET','POST'])
def result():
    if request.method == 'POST':
        m1 = int(request.form['phy'])
        m2 = int(request.form['chem'])
        m3 = int(request.form['math'])

        avg = (m1+m2+m1)/3
        temp = {}
        temp['name'] = request.form['name']
        temp['average'] = avg
        return render_template('result.html',result = temp)

if __name__ == '__main__':
    app.run(debug=True)    