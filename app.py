from flask import Flask, render_template, request, jsonify
import os
import joblib

app = Flask(__name__)

# Load your trained model
with open('phishing_model.pkl', 'rb') as file:
    model = joblib.load(file)

# 🔧 Add your extract_features function here 👇
def extract_features(url):
    feature1 = len(url)
    feature2 = int('login' in url.lower())
    feature3 = int('verify' in url.lower())
    feature4 = int(url.lower().startswith('https'))
    return [feature1, feature2, feature3, feature4]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')

    url_features = [extract_features(url)]  # wraps it in a list because model.predict expects a 2D array
    prediction = model.predict(url_features)

    if prediction[0] == 1:
        result = "⚠️ This URL looks suspicious!"
    else:
        result = "✅ This URL seems safe."

    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

