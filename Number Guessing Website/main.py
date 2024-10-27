from flask import Flask
import random

app = Flask(__name__)

ran_num = random.randint(0, 9)

def check(function):
    def wrapper(num):
        if num < ran_num:
            return '<h1>Too low, try again</h1>'\
            '<iframe src="https://giphy.com/embed/5bgS90uCmWoWp2hBvj" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/westminsterkennelclub-wkcdogshow-wkc-westminsterkennelclubdogshow-5bgS90uCmWoWp2hBvj">via GIPHY</a></p>'
        elif num > ran_num:
            return '<h1>Too high, try again</h1>'\
            '<iframe src="https://giphy.com/embed/Gq0TB6Ltlzz0PhKNfV" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/puppy-doggo-doggie-Gq0TB6Ltlzz0PhKNfV">via GIPHY</a></p>'
        else:
            return '<h1>You got it, congrats!</h1>'\
            '<iframe src="https://giphy.com/embed/Ch0JvNvkk7PH2" width="480" height="269" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/excited-jumping-yay-Ch0JvNvkk7PH2">via GIPHY</a></p>'
    return wrapper

@app.route('/')
def home():
    return '''
    <h1>Guess the number between 0 and 9</h1>
    <iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    <p><a href="https://giphy.com/gifs/animation-retro-pixel-3o7aCSPqXE5C6T8tBC">via GIPHY</a></p>
    '''

@app.route('/<int:num>')
@check
def result(num):
    return str(num)

if __name__ == '__main__':
    app.run(debug=True)
