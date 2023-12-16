import instaloader
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)



L = instaloader.Instaloader()
USER = "scraping78"           # User name
PASSWORD = "sarabjotsceaping"   # Password


L.login(USER, PASSWORD)        

post = instaloader.Post.from_shortcode(L.context, 'C01p7CToOQv')     # Post shortcode Shortcode is the part after the p/ in the URL https://www.instagram.com/p/C01p7CToOQv/?utm_source=ig_web_copy_link&igshid=ODhhZWM5NmIwOQ== 

print(post.owner_username)

with open('output.txt', 'w', encoding='utf-8') as f:
    for comment in post.get_comments():
        f.write(comment.text + '\n')