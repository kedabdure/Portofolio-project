from flask_mail import Message
from app import mail
from . import api_views

# SEND EMAIL
from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)


@api_views.route('/email', methods=['POST'])
def send_email():
    """
    Send email to users.
    """
    data = request.get_json()
    subject = data.get('subject', "Expert handyman")
    message = data.get('massage', "We are going to assign a tasker who is suitable for your need.")
    sender=data.get('sender')
    users = data.get('recipients', []) #list of recipient

    if not users:
        return jsonify({"success": False, "message": "No users provided"}), 400

    try:
        msg = Message(
            subject=subject,
            body=message,
            sender=sender,
            recipients=users
        )
        mail.send(msg)
        print("message sent correctly")
        return jsonify({"success": True, "message": "Emails sent successfully!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500