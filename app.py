# from flask import Flask, request, jsonify
# import joblib

# # Load model and vectorizer
# model = joblib.load("mood_model.pkl")
# vectorizer = joblib.load("mood_vectorizer.pkl")

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()
#     sentence = data.get("text", "")

#     if not sentence.strip():
#         return jsonify({"error": "No input text provided"}), 400

#     vect = vectorizer.transform([sentence])
#     prediction = model.predict(vect)[0]

#     return jsonify({"mood": prediction})

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app) 

model = joblib.load("mood_model.pkl")
vectorizer = joblib.load("mood_vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    sentence = data.get("text", "")
    if not sentence.strip():
        return jsonify({"error": "No input"}), 400

    vect = vectorizer.transform([sentence])
    prediction = model.predict(vect)[0]
    return jsonify({"mood": prediction})

if __name__ == "__main__":
    app.run(debug=True)

