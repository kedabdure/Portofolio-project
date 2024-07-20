from flask_mail import Message
from . import api_views
from flask_mail import Mail
from flask import request, jsonify

mail = Mail()


# SEND EMAIL
@api_views.route('/email', methods=['GET', 'POST'])
def send_email():
    """
    Send email to users.
    """
    data = request.get_json()

    subject = data.get('subject', "Expert handyman")
    message = data.get('message', "We are going to assign a tasker who is suitable for your need.")
    sender = data.get('sender')
    users = data.get('recipients', [])

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
