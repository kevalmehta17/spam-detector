from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

# Load the model from the pickle file

with open('models/spam_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


# Define the API route Endpoint

@app.route('/predict', methods=['POST'])

def predict():
    # get the data from the request from the client
    data  = request.get_json() 
    email = data['email'] #this will extract the email from the request data
    prediction = model.predict([email])[0] 
    result = 'Spam' if prediction == 'spam' else  'Not Spam'
    return jsonify({'prediction':result})

if __name__ == '__main__':
    app.run(port=5000)