from flask import Flask

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/buy')
@make_bold
@make_emphasis
@make_underlined
def buy():
    return "buy!"

if __name__ == '__main__':
    app.run(debug=True)
