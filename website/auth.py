from flask import Blueprint,render_template, request
from flask.helpers import flash

auth= Blueprint("auth",__name__)


@auth.route("/login", methods= ["GET","POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("/sign-up",methods= ["GET","POST"])
def signup():

    if request.method == 'Post':
        mail= request.form.get("email")
        fname= request.form.get('firstName')
        p1= request.form.get('password1')
        p2= request.form.get('password2')

        if len(mail)< 4:
            flash("Email not greater than 4!", category="error")
            
        elif len(fname)<2:
            flash("First name greater than 4!", category="error")
          
        elif p1 != p2:
            flash("passwords do not match!",category="error")
     
        else:
            flash("Success",category="success")
 

    return render_template("sign_up.html",text="BBBBBBBB")