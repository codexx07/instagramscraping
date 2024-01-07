
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
    username = data['username']
    password = data['password']
    postlink = data['postlink']
    
    subprocess.check_call([sys.executable, 'instagram.py', username, password, postlink])

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)