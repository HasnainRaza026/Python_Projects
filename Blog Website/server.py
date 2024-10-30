import requests
from flask import Flask, render_template, request

def request_decorator(function):
    def wraper():
        data = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        return function(data.json())
    return wraper

app = Flask(__name__)

@app.route('/')
@request_decorator
def home(data=None):
    return render_template('index.html', data=data)

@app.route('/blog')
def blog():
    title = request.args.get('title')
    subtitle = request.args.get('subtitle')
    body = request.args.get('body')
    return render_template('blog.html', title=title, subtitle=subtitle, body=body)

if __name__ == '__main__':
    app.run(debug=True)
