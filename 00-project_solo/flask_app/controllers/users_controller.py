from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user_model, class_model, comment_model
from datetime import datetime
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

# dateFormat = "%#m/%#d/%Y %I:%M %p"

@app.route("/")
def index_page():
    return render_template("login.html")

@app.route("/register_form", methods=["POST"])
def register_form():
    data = {
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"],
                "password1": request.form["password1"],
                "password2": request.form["password2"],
                "trainer": request.form["trainer"]
            }

    if user_model.User.validate_user_register_form(data):
        pw_hash = bcrypt.generate_password_hash(request.form['password1'])
        data["password"] = pw_hash
        this_user_id = user_model.User.save_user(data)
        session["user_id"] = this_user_id
        session["first_name"] = request.form["first_name"]
        session["is_trainer"] = request.form["trainer"]
        print("heres the session trainer", session["is_trainer"])
        return redirect("/classes/dashboard")
    return redirect("/")

@app.route("/login_form", methods=["POST"])
def login_form():
    data = {
                "email": request.form["email"],
                "password3": request.form["password3"]
            }
    
    if user_model.User.validate_user_login_form(data):
        this_user = user_model.User.get_user_by_email(data)
        if this_user:
            if bcrypt.check_password_hash(this_user["password"], request.form["password3"]):
                session["user_id"] = this_user["id"]
                session["first_name"] = this_user["first_name"]
                session["is_trainer"] = this_user["trainer"]
                return redirect("/classes/dashboard")
            flash("Invalid credentials. Please try again.", "login")
    return redirect("/")

@app.route("/logout")
def logout_page():
    session.clear()
    return redirect("/")

@app.route("/create_class_comment_form/<int:class_id>", methods=["POST"])
def comment_form(class_id):
    if "user_id" in session:
        data = request.form.to_dict()
        data["class_id"] = class_id
        data["user_id"] = session["user_id"]
        print("whats the data", data) 
        comment_model.Comment.save_comment(data)
        print("does it make it here???")
        return redirect(f'/class/details/{ class_id }')
    return redirect("/")