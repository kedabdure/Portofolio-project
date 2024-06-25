from . import main
from flask import render_template


@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/services', methods=['GET'])
def services():
    return render_template('services.html')


@main.route('/register', methods=['GET'])
def register():
    return render_template('register.html')