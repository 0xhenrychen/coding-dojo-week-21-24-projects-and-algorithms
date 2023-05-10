from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import message_model, class_model, user_model

# @app.route("/messages/create/<int:ride_id>", methods=["POST"])
# def message_form(ride_id):
#     # if "user_id" not in session:
#     #     return redirect("/")
#     print("does it make it to here?")
#     data = request.form.to_dict()
#     data["ride_id"] = ride_id
#     data["user_id"] = session["user_id"]
#     message.Message.save(data)
#     return redirect(f'/rides/details/{ ride_id }')