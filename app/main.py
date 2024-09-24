from flask import Blueprint, request, jsonify
from .message_processor import process_message

main = Blueprint('main', __name__)

@main.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    user_message = data.get('text')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        processed_data = process_message(user_message)

        return jsonify({"response": processed_data})

    except Exception as e:
        print(f"Error processing message: {str(e)}")
        return jsonify({"error": str(e)}), 500
