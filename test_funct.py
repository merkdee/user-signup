from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup.html')


def verify_user(x):
    try:
        if 3 < len(x) < 20:
            return True
    except ValueError:
        return False


def verify_email(x):
    try:
        if x == x:
            return True
        if '@' and '.com' in x:
            return True
    except ValueError:
        return False


@app.route('/signup', methods=['POST'])
def user_valid():
    user_name = request.form['user_name']
    user_pw = request.form['user_pw']
    verify_pw = request.form['verify_pw']
    user_email = request.form['user_email']

    username_error = ''
    userpw_error = ''
    verifypw_error = ''
    useremail_error = ''

    if not verify_user(user_name):
        username_error = 'Not a valid username. Must be between 3 and 20 characters.'
        user_name = ''

    else:
        if len(user_name) > 20 or len(user_name) < 3:
            username_error = 'Not a valid username. Must be between 3 and 20 characters.'
            user_name = ''

    if not verify_user(user_pw):
        username_error = 'Not a valid password length.'
        user_pw = ''

    else:
        if len(user_pw) < 3:
            userpw_error = 'Not a valid password length.'
            user_pw = ''

    if not verify_user(verify_pw):
        verifypw_error = 'Your passwords must match.'
        verify_pw = ''

    else:
        if user_pw != verify_pw:
            userpw_error = 'Your passwords must match.'
            verify_pw = ''

    if not verify_email(user_email):
        useremail_error = 'Please enter your email.eg. name@company.com'
        user_email = ''

    else:
        if len(user_email) < 1:
            useremail_error = 'Please enter your email.eg. name@company.com'
            user_email = ''

    if not username_error and not userpw_error and not useremail_error:
        return render_template('welcome.html', user_name=user_name)

    else:
        if username_error and userpw_error and useremail_error:
            return render_template('verification.html', username_error=username_error, userpw_error=userpw_error,
            verifypw_error=verifypw_error, useremail_error=useremail_error,user_name=user_name, user_pw=user_pw,verify_pw=verify_pw,user_email=user_email)


@app.route("/welcome")
def user_hello():
    user_name = request.args.get('user_name')
    return '<h1> Welcome, {0}!</h1>'.format(user_name)


app.run()
