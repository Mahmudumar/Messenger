from flask import Flask, redirect, render_template, url_for,request,session
from flask_socketio import SocketIO, send

app=Flask(__name__)
app.secret_key = 'Hello'
socketio=SocketIO(app, cors_allowed_origins='*')

  
@app.route('/')
def welcome():
    return '<h1>Welcome to Unanimos</h1>\
        <a href="login">login</a>'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        session['user'] = user
        return redirect(url_for("user"))
    else:
        return render_template('login.html')

@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    if message != "User connected!":
        send(message, broadcast=True)
  
@app.route('/user',methods=['POST','GET'])
def user():
    if 'user' in session:
        user=session["user"]
        return render_template('user.html', username=user)


