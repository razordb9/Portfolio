from application import app
from flask import render_template, redirect, flash, request, Response, json
from application.forms import LoginForm
from application.models import work

@app.route("/")
@app.route("/index")
def index():
    workData = work.objects.all()
    print(workData)
    return render_template("index.html", index=True, workData=workData)

@app.route("/about")
def about():
    return render_template("about.html", about=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit() == True:
        if request.form.get("email") == "thomas.zaussnig@outlook.com":
            flash("You are successfully logged in!")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong")
    return render_template("login.html", form=form, login=True, title='Login')