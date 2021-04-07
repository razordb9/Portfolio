from application import app
from flask import render_template, redirect, flash, request, Response, json, session, url_for
from application.forms import LoginForm, RegisterForm, UpdateUserForm, MyWorkItem, AddMyWorkItem, AddBlogEntry, BlogEntry
from application.models import work, User, blog


##################################################
#               Admin Console                    #
##################################################

@app.route("/adminconsole")
def adminconsole():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('login'))
    return render_template('Adminpage/console.html')

@app.route("/admin", methods=["GET", "POST"])
def login():
    if session.get('username'):
        return redirect(url_for('adminconsole'))
    form = LoginForm()

    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user        = User.objects(email=email).first()
        if user and user.get_password(password):
            flash("You are successfully logged in!", "success")
            session['user_id']      = user.user_id
            session['username']     = user.first_name
            session['lastname']     = user.last_name
            session['email']        = user.email
            session['permission']   = user.permission
            return render_template('Adminpage/console.html')
        else:
            flash("Sorry, something went wrong", "danger")
    return render_template('Adminpage/adminlogin.html', form=form, login=True, title='Login')

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username', None)
    session.pop('lastname', None)
    session.pop('email', None)
    session.pop('permission', None)
    flash("You are successfully logged out!", "warning")
    return redirect(url_for('login'))

@app.route("/adminpage")
def adminpage():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('login'))       #login is the function name which redirects to def login()
    users = User.objects.all()
    return render_template("Adminpage/adminpage.html", adminpage=True, userData=users)

@app.route("/register", methods=["GET", "POST"])
def register():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('login'))
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
    return render_template("Adminpage/register.html", title="Register", form=form, register=True)

@app.route("/myprojects", methods=["GET", "POST"])
def myprojects():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('login'))
    works = work.objects.order_by("work_id")
    return render_template("Adminpage/myprojects.html", mywork=True, workData=works)

@app.route("/blogentries")
def blogentries():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('login'))
    blogs = blog.objects.all()
    return render_template("Adminpage/blogentries.html", blogentries=True, blogData=blogs) 
   
@app.route("/blogentry", methods=["GET", "POST"])
def blogentry():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('index'))

    form        = BlogEntry()

    id          = request.form.get('blog_id')
    title       = request.form.get('title')
    text        = request.form.get('text')
    visibility  = request.form.get('visibility')
    print(visibility)
    return render_template("Adminpage/blogentry.html", form=form, blog={"blog_id":id,"title":title,"text":text,"visibility":visibility})

@app.route("/updateblogentry", methods=["GET", "POST"])    
def updateblogentry(): 
    if request.method == "POST": 
        # getting input with name = fname in HTML form 
        title       = request.form.get("title") 
        print(title)
        # getting input with name = lname in HTML form  
        text        = request.form.get("text")  
        print(text)
        visibility  = request.form.get("visibility")
        print(visibility)

        key         = request.form.get("blog_id")   
        key         = int(key)
        blogitem    = blog.objects(blog_id=key).get()
        if visibility is None:
            blogitem.update(
                title       = request.form.get("title"),
                text        = request.form.get("text"),
                visibility  = False
            )
        else:
            blogitem.update(
                title       = request.form.get("title"),
                text        = request.form.get("text"),
                visibility  = True
            )
        blogitem.reload()
        flash("You successfully updated the blog entry!", "success")    
        return redirect(url_for('blogentries'))   
    else:
        print("failed")
    return render_template("blogentries.html")

@app.route("/addblogentry", methods=["GET", "POST"])    
def addblogentry():    
    if not session.get('permission') == 'Admin':
        return redirect(url_for('index'))
    form = AddBlogEntry()
    if form.validate_on_submit():
        blog_id     = blog.objects.count()
        blog_id    += 1

        title       = form.title.data
        hashTag     = form.hashTag.data
        text        = form.text.data
        visibility  = form.visibility.data

        blogs = blog(blog_id=blog_id, title=title, hashTag=hashTag, text=text, visibility=visibility)
        blogs.save()
        flash("You successfully created a new blog entry","success")
        return redirect(url_for('blogentries'))
    return render_template("Adminpage/addblogentry.html", title="Add new blog entry", form=form, addblogentry=True)

@app.route("/removeblogentry", methods=["GET", "POST"])    
def removeblogentry():    
    try:
        key = request.form.get("blog_id")    
        key = int(key)
        blog.objects(blog_id=key).delete()
        flash("You successfully removed the blog entry!", "success")    
        return redirect(url_for('blogentries'))   
    except:
        flash("You couldn't removed the blog entry!", "danger")    
        return redirect(url_for('blogentries')) 

@app.route("/editpages")
def editpages():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('login'))
    return render_template("Adminpage/editpages.html", editpages=True)

@app.route("/myworkitems", methods=["GET", "POST"])
def myworkitems():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('index'))

    form        = MyWorkItem()

    id          = request.form.get('work_id')
    title       = request.form.get('title')
    description = request.form.get('description')
    return render_template("myworkitems.html", form=form, work={"work_id":id,"title":title,"description":description})

@app.route("/removemyworkitem", methods=["GET", "POST"])    
def removemyworkitem():    
    try:
        key = request.form.get("work_id")    
        key = int(key)
        work.objects(work_id=key).delete()
        flash("You successfully removed the work item!", "success")    
        return redirect(url_for('mywork'))   
    except:
        flash("You couldn't removed the work item!", "danger")    
        return redirect(url_for('myworkitem'))  

@app.route("/updatemyworkitem", methods=["GET", "POST"])    
def updatemyworkitem(): 
    if request.method == "POST": 
        # getting input with name = fname in HTML form 
        title       = request.form.get("title") 
        # getting input with name = lname in HTML form  
        description = request.form.get("description")  

        key         = request.form.get("work_id")    
        key         = int(key)

        workitem    = work.objects(work_id=key).get()
        workitem.update(
            title       = request.form.get("title"),
            description = request.form.get("description")
        )
        workitem.reload()
        flash("You successfully updated the work item!", "success")    
        return redirect(url_for('myprojects'))   
    else:
        print("failed")
    return render_template("myworkitem.html")

@app.route("/addmyworkitem", methods=["GET", "POST"])    
def addmyworkitem():    
    if not session.get('permission') == 'Admin':
        return redirect(url_for('index'))
    form = AddMyWorkItem()
    if form.validate_on_submit():
        work_id     = work.objects.count()
        work_id     += 1

        title       = form.title.data
        description = form.description.data
      

        works       = work(work_id=work_id, title=title, description=description)
        works.save()
        flash("You successfully created a new user!","success")
        return redirect(url_for('mywork'))
    return render_template("Adminpage/addmyworkitem.html", title="Add work Item", form=form, addmyworkitem=True)

##################################################


##################################################
#                Error Pages                     #
##################################################

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('Errorpages/404.html'), 404

##################################################

##################################################
#                Test Pages                      #
##################################################

@app.route("/test")
def test():
    return render_template("test.html")

##################################################

##################################################
#                 Main Pages                     #
##################################################

@app.route("/")
@app.route("/index")
def index():
    workData = work.objects.all()
    blogData = blog.objects().order_by('-blog_id').limit(2)        
    return render_template("index.html", index=True, workData=workData, blogData=blogData)

@app.route("/myblog")
def myblog():
    blogData = blog.objects.order_by('-blog_id')
    return render_template("blog.html", blog=True, blogData=blogData)

@app.route("/mainpage_template")
def mainpage_template():
    return render_template("mainpage_template.html", editpages=True)

@app.route("/user_settings", methods=["GET", "POST"])
def user_settings():
    if not session.get('permission') == 'Admin':
        return redirect(url_for('index'))
    
    form        = UpdateUserForm()

    id          = request.form.get('user_id')
    first_name  = request.form.get('first_name')
    last_name   = request.form.get('last_name')
    email       = request.form.get('email')
    permission  = request.form.get('permission')
    return render_template("user_settings.html", form=form, data={"user_id":id,"first_name":first_name,"last_name":last_name,"email":email,"permission":permission}) 

@app.route("/remove", methods=["GET", "POST"])    
def remove():    
    try:
        key = request.form.get("user_id")    
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
        #first_name  = request.form.get("fname") 
        # getting input with name = lname in HTML form  
        #last_name   = request.form.get("lname")  
        print(request.form.get("perm"))

        key     = request.form.get("user_id")    
        key     = int(key)
        user    = User.objects(user_id=key).get()
        user.update(
            first_name  = request.form.get("fname"),
            last_name   = request.form.get("lname"),
            permission  = request.form.get("perm"),
            email       = request.form.get("email")
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





