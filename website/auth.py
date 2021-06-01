from flask import Blueprint,render_template, request, redirect, url_for
from flask.helpers import flash
from sqlalchemy.engine import url
from sqlalchemy.sql.operators import istrue
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user, current_user


auth= Blueprint("auth",__name__)


@auth.route("/login", methods= ["GET","POST"])
def login():
    if request.method== 'POST':
        mail= request.form.get("email")
        password= request.form.get('password')

        user= User.query.filter_by(email= mail).first()

        if not user:
            flash("Email not found", category="error")
        elif(check_password_hash(user.password, password)):
            flash("Successfuly logged in", category="success")
            login_user(user, remember= True)
            return redirect(url_for("views.home"))
        else:
            flash("Password do not match with the email",category="error")

    return render_template("login.html", user= current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("auth.login"))

@auth.route("/sign-up",methods= ["GET","POST"])
def signup():

    if request.method == 'POST':
        mail= request.form.get("email")
        fname= request.form.get('firstName')
        p1= request.form.get('password1')
        p2= request.form.get('password2')

        user= User.query.filter_by(email= mail).first()

        if user:
            flash("User already exist", category="error")
            return redirect(url_for("auth.login"))

        elif len(mail)< 4:
            flash("Email not greater than 4!", category="error")
            
        elif len(fname)<2:
            flash("First name greater than 4!", category="error")
          
        elif p1 != p2:
            flash("passwords do not match!",category="error")
     
        else:
            flash("Success",category="success")
            new_user= User(mail,fname,generate_password_hash(p1,method="sha256"))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember= True)

            print(new_user)

            return redirect(url_for("views.home"))

 

    return render_template("sign_up.html", user= current_user)