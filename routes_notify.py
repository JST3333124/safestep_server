from flask import Blueprint, request, jsonify
from fcm import send_fcm_to_topic
from auth_utils import decode_token
from models_event import Event
from models_user import User
from database import db

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

@notify_bp.route("/notifications", methods=["GET"])
def get_notifications():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_id = decode_token(token)
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    events = Event.query.filter_by(user_id=user_id).order_by(Event.created_at.desc()).limit(20).all()
    result = []
    for event in events:
        result.append({
            "id": event.id,
            "title": "낙상 감지" if event.type == "fall" else "위치 보고",
            "message": f"{event.type.upper()} 이벤트 수신: {event.created_at.strftime('%Y-%m-%d %H:%M')}"
        })

    return jsonify(result)

@notify_bp.route("/fcm-token", methods=["POST"])
def save_fcm_token():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_id = decode_token(token)
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    fcm_token = data.get("fcm_token")
    if not fcm_token:
        return jsonify({"error": "Missing fcm_token"}), 400

    user = User.query.get(user_id)
    if user:
        user.fcm_token = fcm_token
        db.session.commit()
        return jsonify({"message": "FCM token saved"})
    else:
        return jsonify({"error": "User not found"}), 404
