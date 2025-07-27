from database import db
from datetime import datetime
import json

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # "fall" or "location"
    data = db.Column(db.Text, nullable=False)  # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, type, data):
        self.user_id = user_id
        self.type = type
        self.data = json.dumps(data)
