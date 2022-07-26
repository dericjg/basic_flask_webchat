from flask import render_template, url_for, redirect, request, flash, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from forms import Registration_Form, Login_Form
from config import app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_socketio import SocketIO, emit, send


login_manager = LoginManager()
login_manager.init_app(app)
socketio = SocketIO(app)

from db_schema import User, Message, Chatroom, db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        uname = form.username.data
        pword = form.password.data

        user = User.query.filter(User.username==uname).first()
        print(user.username)
        print(user.password)
        print(user.email)

        if user:
            if check_password_hash(user.password, pword):
                print('Passwords match')
                login_user(user)
                return redirect(url_for('profile'))
            else:
                print('Password is incorrect.')
        else:
            flash('Invalid username.')
            print('Invalid username.')

    return render_template('login.html', form=form)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = Registration_Form()
    if form.validate_on_submit():
        uname = form.username.data
        pword = generate_password_hash(form.password.data)
        mail = form.email.data

        db.session.add(User(username=uname, password=pword, email=mail))

        try:
            db.session.commit()
        except:
            db.session.rollback()

        return redirect(url_for('login'))

    return render_template('signup.html' ,form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')

@app.route('/chatroom', methods=['GET', 'POST'])
@login_required
def chatroom():
    return render_template('chatroom.html')

@socketio.on('user_connected')
def handle_message(data):
    emit('user_connected', f'{data} has connected!', broadcast=True)

@socketio.on('user_message')
def handle_message(data):
    
    emit('user_message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
