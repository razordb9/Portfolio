from application import app
from flask import render_template, redirect, flash, request, Response, json, session, url_for
from application.forms import LoginForm, RegisterForm
from application.models import work, User

@app.route("/")
@app.route("/index")
def index():
    workData = work.objects.all()
    return render_template("index.html", index=True, workData=workData)

@app.route("/user_settings")
def user_settings():
    userData = User.objects.all()
    return render_template("user_settings.html", userData=userData)

@app.route("/about")
def about():
    return render_template("about.html", about=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('username'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash("You are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong", "danger")
    return render_template("login.html", form=form, login=True, title='Login')

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)