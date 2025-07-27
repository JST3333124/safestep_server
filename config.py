import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("firebase-adminsdk.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

FCM_CREDENTIALS = cred
