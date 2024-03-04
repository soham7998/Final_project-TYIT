from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)

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
        return redirect(url_for('index'))  # Redirect to the index page after successful login
    else:
        flash('Login failed. Invalid username or password.', 'error')  # Flash an error message
        return redirect(url_for('login'))  # Redirect to the login page on login failure



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/DA')
def data_analyst():
    return render_template('DA.html')

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


