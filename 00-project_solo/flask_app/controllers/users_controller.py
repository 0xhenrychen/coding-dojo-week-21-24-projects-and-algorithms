from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user_model, class_model, message_model
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
        this_user_id = user_model.User.save(data)
        session["user_id"] = this_user_id
        session["first_name"] = request.form["first_name"]
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
                return redirect("/classes/dashboard")
            flash("Invalid credentials. Please try again.", "login")
        # return redirect("/")
    return redirect("/")

@app.route("/logout")
def logout_page():
    session.clear()
    return redirect("/")

# @app.route("/messages/create/<int:ride_id>", methods=["POST"])
# def message_form(ride_id):
#     if "user_id" not in session:
#         return redirect("/")
#     data = request.form.to_dict()
#     data["ride_id"] = ride_id
#     data["user_id"] = session["user_id"] 
#     message_model.Message.save(data)
#     return redirect(f'/rides/details/{ ride_id }')