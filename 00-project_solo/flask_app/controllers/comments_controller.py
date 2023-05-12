from flask_app import app
from flask import redirect, request, session
from flask_app.models import comment_model

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