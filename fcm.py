import firebase_admin
from firebase_admin import credentials, messaging
import config

cred = credentials.Certificate(config.FCM_CREDENTIALS)
firebase_admin.initialize_app(cred)

def send_fcm_to_token(token: str, title: str, body: str):
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        token=token
    )
    response = messaging.send(message)
    return response

def send_fcm_to_topic(topic: str, title: str, body: str):
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        topic=topic
    )
    response = messaging.send(message)
    return response
