from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load

app = Flask(__name__)
CORS(app)

# Load the model from the pickle file

model = load('../models/spam_classifier.joblib')
vectorizer = load('../models/vectorizer.joblib')

@app.route('/predict',methods=["POST"])

def predict():
    data = request.json
    message = data.get("text","")

    if not message:
        return jsonify({"error":"No message Provided"}), 400

    message_tfidf = vectorizer.transform([message])
    prediction = model.predict(message_tfidf)[0]

    return jsonify({"prediction":"spam" if prediction == 1 else "Not-Spam"})


if __name__ == '__main__':
    app.run(port=5000,debug=True)