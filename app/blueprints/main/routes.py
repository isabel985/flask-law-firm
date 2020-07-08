from . import main as app
from flask import flash, redirect, url_for, render_template
from app import db
from app.models import Member

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