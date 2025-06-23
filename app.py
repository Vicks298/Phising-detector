from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')

    # 🔍 Simple fake detection logic — replace with your actual detection logic
    if "login" in url or "verify" in url or "update" in url:
        result = ["⚠️ This URL looks suspicious!"]
    else:
        result = ["✅ This URL seems safe."]

    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
