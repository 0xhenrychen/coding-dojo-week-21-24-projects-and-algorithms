from flask_app import app
from flask_app.controllers import users_controller, classes_controller, messages_controller

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5009)