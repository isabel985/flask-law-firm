from app import app
from .models import Member
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/team')
def team():
    context = {'members': Member.query.all()}
    return render_template('team.html', **context)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

