from flask import Flask, render_template, request, jsonify
import os
import pickle

# Load your trained model
with open('phishing_model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')

    # Convert the URL into the format your model expects
    # This will depend on how you trained your model.
    # Example: if you trained it on URL length and number of dots
    url_features = [[len(url), url.count('.')]]

    # Use model to predict
    prediction = model.predict(url_features)

    if prediction[0] == 1:
        result = ["⚠️ This URL looks suspicious!"]
    else:
        result = ["✅ This URL seems safe."]

    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

