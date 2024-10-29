import requests
from flask import Flask
from flask import render_template

def request_data_decorator(func):
    def wrapper(name, *args, **kwargs):
        age_response = requests.get(f"https://api.agify.io?name={name}")
        gender_response = requests.get(f"https://api.genderize.io?name={name}")
        
        age_data = age_response.json().get("age")
        gender_data = gender_response.json().get("gender")
        
        return func(name, age_data, gender_data)
    return wrapper


app = Flask(__name__)

@app.route('/guess/<name>')
@request_data_decorator
def home(name, age=None, gender=None):
    return render_template('index.html', name=name, age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)