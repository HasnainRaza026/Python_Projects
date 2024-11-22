from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message=('must enter email'))])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message=('Password must contain atleast 8 characters'))])
    submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # form is submited successfully (POST request) (returns true)
        if form.email.data=="admin@email.com" and form.password.data=="12345678":
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)