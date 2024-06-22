from . import main
from flask import jsonify

@main.route('/api/handymen', methods=['GET'])
def get_handymen():
    handymen = [
        {'id': 1, 'name': 'John Doe', 'specialty': 'Plumbing'},
        {'id': 2, 'name': 'Jane Smith', 'specialty': 'Electrical'}
    ]
    return jsonify(handymen)
