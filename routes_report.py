from flask import Blueprint, request, jsonify
from models_event import Event
from database import db
from auth_utils import decode_token

report_bp = Blueprint("report", __name__)

@report_bp.route("/fall", methods=["POST"])
def report_fall():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_id = decode_token(token)
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    event = Event(user_id=user_id, type="fall", data=data)
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": "Fall reported"})


@report_bp.route("/location", methods=["POST"])
def report_location():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_id = decode_token(token)
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    event = Event(user_id=user_id, type="location", data=data)
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": "Location reported"})
