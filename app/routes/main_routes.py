from . import main
from flask import render_template


@main.route('/', methods=['GET'])
def index():
    return "<h1>HOME PAGE</h1>"


@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@main.route('contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@main.route('blogs', methods=['GET'])
def get_blogs():
    return render_template('blogs.html')
