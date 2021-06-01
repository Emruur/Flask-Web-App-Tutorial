from flask import Blueprint, render_template
from flask.globals import request
from flask.helpers import flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views= Blueprint("views",__name__)

@views.route("/", methods= ["GET","POST"])
@login_required
def home():
    if request.method == "POST":
        note= request.form.get("note")
        new_note= Note(note)

        new_note.user_id= current_user.id

        db.session.add(new_note)
        db.session.commit()

        flash("Note added!", category= "success")

        for note in current_user.notes:
            print("note= "+note.note)



    return render_template("home.html", user= current_user )

 