
from flask import Flask, request, jsonify, send_from_directory
import os
import subprocess
import sys

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    username = request.form.get('username')
    password = request.form.get('password')
    shortcode = request.form.get('shortcode')

    if username is None or password is None or shortcode is None:
        return jsonify({'status': 'error', 'message': 'Missing username, password, or shortcode'}), 400

    subprocess.check_call([sys.executable, 'instagram.py', username, password, shortcode])

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)