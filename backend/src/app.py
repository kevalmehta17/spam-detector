from flask import Flask, jsonify, request
from joblib import load

app = Flask(__name__)

# Load the model from the pickle file

model = load('../models/spam_classifier.joblib')
vectorizer = load('../models/vectorizer.joblib')

@app.route('/predict',methods=["POST"])

def predict():
    data = request.json
    message = data.get("message","")

    message_tfidf = vectorizer.transform([message])
    prediction = model.predict(message_tfidf)[0]

    return jsonify({"predicition":"spam" if prediction == 1 else "Not-Spam"})


if __name__ == '__main__':
    app.run(port=5000,debug=True)