
from flask import Flask, request, jsonify, send_from_directory
import os
import subprocess
from subprocess import CalledProcessError
import sys

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        shortcode = data.get('shortcode')

        if username is None or password is None or shortcode is None:
            return jsonify({'status': 'error', 'message': 'Missing username, password, or shortcode'}), 400

        subprocess.check_call([sys.executable, 'instagram.py', username, password, shortcode])
    except CalledProcessError as e:
        return jsonify({'status': 'error', 'message': 'An error occurred while scraping: {}'.format(e)}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'An unexpected error occurred: {}'.format(e)}), 500

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)