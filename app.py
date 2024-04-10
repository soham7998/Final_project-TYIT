from flask import Flask, render_template, request, make_response,redirect, url_for, flash , session
from pymongo import MongoClient
import secrets
import time

app = Flask(__name__)
app.secret_key = secrets.token_hex(16) 

# Function to check if the session has expired
def session_expired():
    if 'login_time' in session:
        # Check if the session is expired (5 minutes)
        return time.time() - session['login_time'] > 300
    return True


@app.route('/database', methods=['POST'])
def button_click():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    client = MongoClient('mongodb+srv://sohamshahh:soham2003@cluster0.x5owqbs.mongodb.net/')
    db = client['mydatabase']
    users_collection = db['users']

    user_data = {'username': username, 'email': email, 'password': password}
    users_collection.insert_one(user_data)

    
    print(f"Username: {username}, Email: {email}, Password: {password}")
    return render_template('login.html')

@app.route('/databaselogin', methods=['POST'])
def submit_login():
    username = request.form.get('username')
    password = request.form.get('password')

    client = MongoClient('mongodb+srv://sohamshahh:soham2003@cluster0.x5owqbs.mongodb.net/')
    db = client['mydatabase']
    users_collection = db['users']

    # Retrieve user by username
    query = {'username': username, 'password': password}
    user = users_collection.find_one(query)

    if user:
        flash('Login successful!', 'success')  # Flash a success message
        session['username'] = username  # Set the username in the session
        session['login_time'] = time.time()  # Set the login time
        response = make_response(redirect(url_for('index')))

        # Set cookies
        response.set_cookie('isAuthenticated', 'true')

        return response  
        # return redirect(url_for('index'))  # Redirect to the index page after successful login
    else:
        flash('Login failed. Invalid username or password.', 'error')  # Flash an error message
        return redirect(url_for('login'))  # Redirect to the login page on login failure
 


@app.route('/logout')
def logout():
    session.clear()  # Clear the session data
    return redirect(url_for('login'))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/DA')
def data_analyst():
    return render_template('DA.html')

@app.route('/selfpractice')
def selfpractice():
    return render_template('selfpractice.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/DE')
def data_engineer():
    return render_template('DE.html')

@app.route('/DS')
def data_science():
    return render_template('DS.html')

@app.route('/about')
def about():
    return render_template('about.html')


