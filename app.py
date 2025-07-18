from flask import Flask, render_template, abort
from posts import posts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        abort(404)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
