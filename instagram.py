from flask import Flask, request, send_file
import instaloader
import csv
import os
import logging

app = Flask(__name__)

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
        with open('comments.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Comments'])
            for comment in comments:
                writer.writerow([comment])

        return {'message': 'Comments scraped successfully'}

    except Exception as e:
        app.logger.error(e)  
        return str(e), 500   

@app.route('/download', methods=['GET'])
def download():
    if os.path.exists('comments.csv'):
        return send_file('comments.csv', as_attachment=True)
    else:
        return {'message': 'No file to download'}

if __name__ == '__main__':
    app.logger.setLevel(logging.ERROR)
    app.run(debug=True, port=5001)