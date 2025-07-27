import os
import json
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"]))

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

FCM_CREDENTIALS = cred
