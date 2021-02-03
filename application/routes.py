from application import app
from flask import render_template, redirect, flash, request, Response, json, session, url_for
from application.forms import LoginForm, RegisterForm, UpdateUserForm
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
    
    form = UpdateUserForm()

    id = request.form.get('user_id')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    permission = request.form.get('permission')
    return render_template("user_settings.html", form=form, data={"user_id":id,"first_name":first_name,"last_name":last_name,"email":email,"permission":permission}) 

@app.route("/requestTest", methods=["GET", "POST"])
def requestTest():
    if request.method == "POST": 
        # getting input with name = fname in HTML form 
        first_name = request.form.get("fname") 
        # getting input with name = lname in HTML form  
        last_name = request.form.get("lname")  
        return "Your name is "+first_name + last_name 
    return render_template("requestTest.html")

@app.route("/remove", methods=["GET", "POST"])    
def remove():    
    try:
        key=request.form.get("user_id")    
        key = int(key)
        User.objects(user_id=key).delete()
        flash("You successfully removed the user!", "success")    
        return redirect(url_for('adminpage'))   
    except:
        flash("You couldn't removed the user!", "success")    
        return redirect(url_for('user_settings'))   

@app.route("/updateuser", methods=["GET", "POST"])    
def updateuser(): 
    if request.method == "POST": 
        # getting input with name = fname in HTML form 
        first_name = request.form.get("fname") 
        # getting input with name = lname in HTML form  
        last_name = request.form.get("lname")  

        key=request.form.get("user_id")    
        key = int(key)
        user = User.objects(user_id=key).get()
        user.update(
            first_name = request.form.get("fname"),
            last_name = request.form.get("lname"),
            email = request.form.get("email")
        )
        user.reload()
        flash("You successfully updated the user!", "success")    
        return redirect(url_for('adminpage'))   
    else:
        print("failed")
    return render_template("adminpage.html")

    #try:
    #    if request.method == 'POST':
    #        key=request.form.get("user_id")    
    #        key = int(key)
    #        user = User.objects(user_id=key).get()
    #        print(user.user_id)
    #        print(request.form.get("firstname"))
    #        print(request.form.get("last_name"))
    #        print(request.form.get("email"))
    #        user.update(
    #            first_name = request.form.get("fname"),
    #            last_name = request.form.get("lname"),
    #            email = request.form.get("email")
    #        )
    #        user.reload()
    #        flash("You successfully updated the user!", "success")    
    #        return redirect(url_for('adminpage'))   
    #except:
    #    flash("You couldn't update the user!", "success")    
    #    return redirect(url_for('adminpage')) 

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