# from flask import jsonify, request
# from .. import api_v1
# from flask_mail import Mail, Message

# mail = Mail()

# @api_v1.route('/email', methods=['POST'])
# def send_email():
#     data = request.get_json()
#     subject = data.get('subject', 'Expert handyman')
#     message = data.get('message', 'We are going to assign a tasker who is suitable for your need.')
#     sender = data.get('sender', 'your-email@example.com')
#     recipients = data.get('recipients', [])

#     if not recipients:
#         return jsonify({"success": False, "message": "No recipients provided"}), 400

#     try:
#         msg = Message(
#             subject=subject,
#             sender=sender,
#             recipients=recipients
#         )
#         msg.body = message
#         msg.html = f"""
#         <html>
#             <body>
#                 <p>{message}</p>
#             </body>
#         </html>
#         """
#         mail.send(msg)
#         return jsonify({"success": True, "message": "Emails sent successfully!"})
#     except Exception as e:
#         return jsonify({"success": False, "message": str(e)}), 500
