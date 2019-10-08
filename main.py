from flask import Flask, request, request, render_template
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

@app.route("/signup", methods=['POST'])
def user_valid(user_name):
    user_name = request.form['user_name']
    user_pw = request.form['user_pw']
    verify_pw = request.form['verify_pw']
    user_email = request.form['user_email']
    
    user_name_char = user_name.char
    if user_name_char is not > 3 and user_name_char is not < 20:
        username_error = 'Not a valid username. Must be between 3 and 20 characters.'
        user_name = ''
    else:
        if user