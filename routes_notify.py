from flask import Blueprint, request, jsonify
from fcm import send_fcm_to_topic
from auth_utils import decode_token

notify_bp = Blueprint("notify", __name__)

@notify_bp.route("/push", methods=["POST"])
def push():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_id = decode_token(token)
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    title = data.get("title", "SafeStep 알림")
    body = data.get("body", "새로운 이벤트가 발생했습니다")

    try:
        response = send_fcm_to_topic("protector_topic", title, body)
        return jsonify({"message": "Notification sent", "response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
