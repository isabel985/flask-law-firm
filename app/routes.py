from app import app, db
from .models import Member, User
from flask import render_template, request, redirect, url_for, flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print('Your input has been submitted!')
        return redirect(url_for('contact'))
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            return redirect(url_for('register'))

        u = User(first_name=first_name, last_name=last_name, email=email, password=password)
        u.generate_password(u.password)

        db.session.add(u)
        db.session.commit()
        flash("User registered successfully")
        return redirect(url_for('login'))
    return render_template('register.html')