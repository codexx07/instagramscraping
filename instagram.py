from flask import Flask, request, send_file
import instaloader
import csv
import os

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    username = request.form.get('username')
    password = request.form.get('password')
    shortcode = request.form.get('shortcode')

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

@app.route('/download', methods=['GET'])
def download():
    if os.path.exists('comments.csv'):
        return send_file('comments.csv', as_attachment=True)
    else:
        return {'message': 'No file to download'}

if __name__ == '__main__':
    app.run(debug=True)