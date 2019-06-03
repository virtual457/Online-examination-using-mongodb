from flask import Flask, render_template,url_for,request,session,redirect, make_response
from hashlib import sha256
from werkzeug import secure_filename
import os
import pymongo

app=Flask(__name__)
app.config['SECRET_KEY']=b'N\x83Y\x99\x04\xc9\xcfI\xb7\xfc\xce\xd1\xcf\x01\xa8\xccr\xbb&\x1b\x11\xac\xc7V'
app.config['MAX_CONTENT_PATH']=1024

client = pymongo.MongoClient("127.0.0.1",27017)
db = client.mongo_exam

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/teacher', methods=['GET','POST'])
def teacher():
    if request.method == 'POST' or request.cookies.get('loggedin')=="True" :
        n = len(list(db.question.find()))
        resp = make_response(render_template('teacher.html',loggedin=True,no=str(n)))
        resp.set_cookie('loggedin','True')
        return resp
    return render_template('teacher.html')

@app.route('/student', methods=['GET','POST'])
def student():
    if request.method == 'POST' :
        resp = make_response(redirect('/questions'))
        resp.set_cookie('stest','started')
        return resp
    return render_template('student.html')

@app.route('/questions', methods=['GET','POST'])
def questions():
    qu = [list(i.values()) for i in list(db.question.find())]
    print(qu)
    return render_template('questions.html', questions=qu, test=True)

@app.route('/logout', methods=['GET','POST'])
def logout():
    resp = make_response(redirect('/teacher'))
    resp.set_cookie('loggedin','False')
    return resp

@app.route('/addquestion', methods=['GET','POST'])
def addquestion():
    if request.method == 'POST':
        q = request.form['qname']
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        ans = request.form['answer']
        db.question.insert_one({'q':q,'a':a,'b':b,'c':c,'d':d,'ans':ans})
        return redirect('/teacher')

@app.route('/delq', methods=['GET','POST'])
def delq():
    db.question.remove({})
    return redirect('/teacher')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        qu = list(db.question.find())
        answers = [ i['ans'] for i in qu]
        given_answer = []
        for i in range(len(qu)):
            given_answer.append(request.form["answer" + str(i+1)])
        ans = [int(answers[i]==given_answer[i]) for i in range(len(answers))]
        p = (sum(ans)/len(ans))*100
        print(answers)
        print(given_answer)
        return render_template('submit.html',percentage=p)

@app.errorhandler(404)
def not_found(e):
    return redirect("/index")

if __name__=='__main__':
    app.run(debug=True)
