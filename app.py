from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-url', methods=['POST'])
def check_url():
    url = request.json['url']
    result = []

    ip_pattern = r'^(http:\/\/|https:\/\/)?(\d{1,3}\.){3}\d{1,3}'
    if re.match(ip_pattern, url):
        result.append("⚠️ Suspicious: URL contains an IP address.")

    domain_parts = url.replace("http://", "").replace("https://", "").split('.')
    if len(domain_parts) > 3:
        result.append("⚠️ Suspicious: URL has multiple subdomains.")

    keywords = ['login', 'verify', 'update', 'secure', 'account']
    for word in keywords:
        if word in url.lower():
            result.append(f"⚠️ Contains suspicious keyword: '{word}'.")

    if not result:
        result.append("✅ URL looks clean (basic checks).")

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
