# import instaloader
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)



# L = instaloader.Instaloader()
# USER = "scraping78"           # User name
# PASSWORD = "sarabjotsceaping"   # Password
# SHORTCODE = "C01p7CToOQv"


# L.login(USER, PASSWORD)        

# post = instaloader.Post.from_shortcode(L.context, SHORTCODE)     # Post shortcode Shortcode is the part after the p/ in the URL https://www.instagram.com/p/C01p7CToOQv/?utm_source=ig_web_copy_link&igshid=ODhhZWM5NmIwOQ== 

# print(post.owner_username)

# with open('output.csv', 'w', encoding='utf-8') as f:
#     for comment in post.get_comments():
#         f.write(comment.text + '\n')


from flask import Flask, request
import instaloader

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

    return {'comments': comments}

if __name__ == '__main__':
    app.run(debug=True)