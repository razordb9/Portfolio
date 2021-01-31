from application import app
from flask import render_template, redirect, flash, request, Response, json, session, url_for
from application.forms import LoginForm, RegisterForm
from application.models import work, User

@app.route("/")
@app.route("/index")
def index():
    workData = work.objects.all()
    return render_template("index.html", index=True, workData=workData)

@app.route("/user_settings", methods=["GET", "POST"])
def user_settings():
    if not session.get('username'):
        return redirect(url_for('index'))

    user_id = request.form.get(user_id)
    first_name = request.form.get(first_name)
    last_name = request.form.get(last_name)
    email = request.form.get(email)
    permission = request.form.get(permission)

    #return render_template("enrollment.html", enrollment=True, data={"id":id,"title":title,"term":term})   
    return render_template("user_settings.html", data={"id":user_id,"first_name":first_name,"last_name":last_name,"email":email,"permission":permission}) 

@app.route("/about")
def about():
    return render_template("about.html", about=True)

@app.route("/adminpage")
def adminpage():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('index'))
    users = User.objects.all()
    return render_template("adminpage.html", about=True, userData=users)

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
            session['lastname'] = user.last_name
            session['email'] = user.email
            session['permission'] = user.permission
            return redirect("/index")
        else:
            flash("Sorry, something went wrong", "danger")
    return render_template("login.html", form=form, login=True, title='Login')

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username', None)
    session.pop('lastname', None)
    session.pop('email', None)
    session.pop('permission', None)
    flash("You are successfully logged out!", "warning")
    return redirect(url_for('index'))

@app.route("/register", methods=["GET", "POST"])
def register():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data
        permission  = form.permission.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name, permission=permission)
        user.set_password(password)
        user.save()
        flash("You successfully created a new user!","success")
        return redirect(url_for('adminpage'))
    return render_template("register.html", title="Register", form=form, register=True)