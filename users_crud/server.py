from flask_app import app
from flask_app.controllers import user_controller
from flask_app.models.user_model import user_model

if __name__ == "__main__":
    app.run(debug=True, port =5001)
