from flask import Blueprint, render_template


auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')


@auth.route('/booking', methods=['GET', 'POST'])
def booking():
    return render_template('booking.html')
