import joblib
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import pos_tag
import string
from flask import Flask,render_template, request


swords = stopwords.words('english')
wnl = WordNetLemmatizer()
app = Flask(__name__,template_folder='template')


def clean_text(text):
    token1 = word_tokenize(text)
    token2 = [word.lower() for word in token1 if word not in string.punctuation]
    token3 = [word for word in token2 if word.lower() not in swords]
    token4 =[]
    tags = pos_tag(token3)
    for word in tags:
        if word[1].startswith('N'):
            token4.append(wnl.lemmatize(word[0],pos = 'n'))
        if word[1].startswith('V'):
            token4.append(wnl.lemmatize(word[0],pos = 'v'))
        if word[1].startswith('R'):
            token4.append(wnl.lemmatize(word[0],pos = 'r'))
        if word[1].startswith('J'):
            token4.append(wnl.lemmatize(word[0],pos = 'a'))
    return token4




classifier = joblib.load('model1.bin')
tfidf = joblib.load('vectorized.bin')


@app.route('/')
def route():
    return render_template('spamdetector.html')

@app.route('/spamfinder',methods =['GET','POST'])
def result():

    if request.method == 'POST':
        data = dict(request.form)
        message = tfidf.transform([data['message']])
        data['result'] = classifier.predict(message[0])
        return render_template('spamout.html', data = data)


if __name__ == '__main__':
    app.run(debug=True)    