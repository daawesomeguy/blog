#!/usr/bin/env python3
"""
Generate static HTML files from Flask blog for GitHub Pages
"""
import os
from posts import posts

def generate_index():
    """Generate the main index.html file"""
    html_content = '''<!doctype html>
<html>
<head>
    <title>blog</title>
    <style>
        body { font-family: 'CMU Serif', serif; margin: 40px; background-color: #eeeedd	; }
        h1 { color: #333; text-align: center; margin-left: 0; }
        h2 {
            color:#3d9e9e; 
            font-size: 3em;
            font-family: 'CMU Serif', serif;
            text-align: center;
            margin-bottom: 30px;
        }
        .typewriter {
            overflow: hidden;
            border-right: 3px solid #3d9e9e;
            white-space: nowrap;
            margin: 0 auto;
            letter-spacing: 0.1em;
            animation: typing 3s steps(9, end) forwards, blink-caret 0.75s step-end infinite;
            display: inline-block;
            width: 0;
        }
        @keyframes typing {
            from { width: 0 }
            to { width: 10.5ch }
        }
        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: #3d9e9e }
        }
        article { 
            margin: 20px auto; 
            padding: 20px; 
            border-bottom: 1px solid #ddd; 
            max-width: 400px; 
            background-color: #f0f0e6;
            border: 1px solid #e6e6d6;
            border-radius: 5px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }
        article:last-child { border-bottom: none; }
        article h3 { margin: 0 0 10px 0; text-align: left; font-size: 2em; }
        article img { width: 100%; height: 100%; object-fit: cover; border-radius: 5px; margin-bottom: 10px; max-height: 500px; }
        a { color: #cda2cf; text-decoration: none;}
    </style>
</head>
<body>
    <h2 class="typewriter">ramblings</h2>
'''
    
    # Add articles
    for post in posts:
        html_content += f'''    <article>
        <a href="post{post['id']}.html">
            <img src="{post['image']}" alt="{post['title']}">
            <h3>{post['title']}</h3>
        </a>
    </article>
'''
    
    html_content += '''</body>
</html>'''
    
    return html_content

def generate_post(post):
    """Generate individual post HTML"""
    html_content = f'''<!doctype html>
<html>
<head>
    <title>{post['title']} - blog</title>
    <style>
        body {{ font-family: 'CMU Serif', serif; margin: 40px; background-color: #eeeedd; }}
        h1 {{ color: #333; text-align: center; margin-left: 0; }}
        a {{ color: #cda2cf; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .back-link {{ margin-bottom: 20px; }}
        article {{ margin: 20px auto; max-width: 600px; }}
        article h1 {{ margin-bottom: 15px; }}
        article img {{ width: 100%; height: 300px; object-fit: cover; border-radius: 5px; margin-bottom: 20px; }}
        article p {{ line-height: 1.6; }}
    </style>
</head>
<body>
    <div class="back-link">
        <a href="index.html">&larr; Back to all posts</a>
    </div>
    
    <article>
        <h1>{post['title']}</h1>
        <img src="{post['image']}" alt="{post['title']}">
        <p>{post['body']}</p>
    </article>
</body>
</html>'''
    
    return html_content

def main():
    """Generate all static files"""
    # Create docs directory for GitHub Pages
    os.makedirs('docs', exist_ok=True)
    
    # Generate index.html
    with open('docs/index.html', 'w') as f:
        f.write(generate_index())
    
    # Generate individual post pages
    for post in posts:
        with open(f'docs/post{post["id"]}.html', 'w') as f:
            f.write(generate_post(post))
    
    print("Static site generated in 'docs' folder!")
    print("Files created:")
    print("- docs/index.html")
    for post in posts:
        print(f"- docs/post{post['id']}.html")

if __name__ == '__main__':
    main()
