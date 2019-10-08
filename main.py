from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def user_hello():
    user_name = request.form['user_name']
    return render_template('welcome.html', user_name=user_name)

def is_string(user_name):
	user_name = request.form['user_name']
	try:
		str(user_name)
		return True
	except ValueError:
		return False

def pw_rules(user_pw):
    user_pw = request.form['user_pw']
    try:
        not user_pw.isspace()
        return True
    except ValueError:
        return False

def verify_email(user_email):
    user_email = request.form['user_email']
    try:
        if '@' and 'com' in user_email:
            return True
    except ValueError:
        return False
            

@app.route("/signup", methods=['POST'])
def user_valid():
    user_name = request.form['user_name']
    user_pw = request.form['user_pw']
    verify_pw = request.form['verify_pw']
    user_email = request.form['user_email']
    
    username_error = ''
    userpw_error = ''
    verifypw_error = ''
    useremail_error = ''
    
    if not is_string(user_name):
        username_error = 'Not a valid username. Must be between 3 and 20 characters.'
        user_name = ''
    else:
        if user_name > 20 and user_name < 3:
            username_error = 'Please select a username between 3 and 20 characters.'
            user_name = ''

    if not pw_rules(user_pw):
        userpw_error = "Not a vaild password. Please enter atleast 8 characters."
        user_pw = ''
    else:
        if len(user_pw) < 8:
            userpw_error = 'Your password must be atleast 8 characters long.'
            user_pw = ''
    
    if user_pw != verify_pw:
        verifypw_error = 'Your passwords must match.'
        verify_pw = ''
    
    if not verify_email(user_email):
        useremail_error = ' Please enter your email.'
        user_email = ''
    else:
        user_email = str(user_email)
        if '@' and '.com' not in user_email:
            useremail_error = 'Please enter your email.'
            user_email = '' 

    if not username_error and userpw_error and useremail_error:
        return render_template('welcome.html', user_name=user_name)
    else:
        return render_template('signup.html', username_error=username_error, userpw_error=userpw_error, verifypw_error=verifypw_error, useremail_error=useremail_error)

app.run()

        