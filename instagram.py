from flask import Flask, request, send_from_directory,send_file
import instaloader
import csv
import os
import logging
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        shortcode = request.json.get('shortcode')

        L = instaloader.Instaloader()
        L.login(username, password)

        post = instaloader.Post.from_shortcode(L.context, shortcode)

        comments = []
        for comment in post.get_comments():
            comments.append(comment.text)

        # Save comments to a CSV file
        with open('./output/comments.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Comments'])
            for comment in comments:
                writer.writerow([comment])

        return {'status':'success','message': 'Comments scraped successfully'}

    except Exception as e:
        app.logger.error("error" + str(e)) 
        return {'status': 'error', 'message': str(e)}, 500   

@app.route('/download', methods=['GET'])
def download():
    if os.path.exists('./output/comments.csv'):
        return send_file('./output/comments.csv', as_attachment=True)
    else:
        return {'message': 'No file to download'}

if __name__ == '__main__':
    app.logger.setLevel(logging.ERROR)
    app.run(debug=True, port=5001)