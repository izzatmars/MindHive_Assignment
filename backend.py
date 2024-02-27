from flask import Flask, request, jsonify
# from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
# from dotenv import load_dotenv
import os
import json

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate("C:/Users/izzat/OneDrive/Desktop/MindHive Assignment/MindHive_Assignment/subway-scraper-firebase-adminsdk-y1xwg-647b4207ad.json")
firebase_app = initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    return 'Hello, Worldi!'

@app.route('/outlets', methods=['GET'])
def get_outlets():
    # Get reference to Firestore collection
    subway_locations_ref = db.collection('subway_locations')

    # Retrieve all documents from the collection
    subway_locations = subway_locations_ref.get()

    # Prepare data to return
    outlets = []
    for doc in subway_locations:
        doc_data = doc.to_dict()
        outlet = {
            'address': doc_data['address'],
            'latitude': doc_data.get('latitude', None),  # Get latitude if exists, otherwise set to None
            'longitude': doc_data.get('longitude', None),  # Get longitude if exists, otherwise set to None
            'name': doc_data['name']
        }
        outlets.append(outlet)

    # Return data as JSON response
    return jsonify(outlets)

if __name__ == '__main__':
    app.run(debug=True)