from flask import Flask, redirect, url_for, render_template, flash
from flask_restful import Resource, Api, reqparse
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'f123321e35e96448d4df72412491729b'

songs = [
    {
        'Artist': 'Eminem',
        'Genre': 'Rap',
        'Song_Name': 'Beautiful',
        'Date_released': 'May 26, 2011'
    },
    {
        'Artist': 'Kendric Lamar',
        'Genre': 'Rap',
        'Song_Name': 'Humble',
        'Date_released': 'June 26, 2010'
    }
]

# Two routes can be handled by same function
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', songs=songs)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        flash(f'Account created for { register_form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=register_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    print("Entered into admin form")
    if login_form.validate_on_submit():
        print("Entered into admin validation")
        if login_form.email.data == 'admin@blog.com' and login_form.password.data == 'password':
            print("Entered into admin block")
            flash(f'You have been logged in! for { login_form.username.data }', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=login_form)


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == '__main__':
    # run our Flask app
    app.run(debug=True)