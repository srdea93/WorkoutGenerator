from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from WorkoutApp.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

# add logger config here

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from WorkoutApp.main.routes import main_blueprint
    from WorkoutApp.exercise.routes import exercise_blueprint
    from WorkoutApp.workout.routes import workout_blueprint
    from WorkoutApp.user.routes import user_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(exercise_blueprint)
    app.register_blueprint(workout_blueprint)
    app.register_blueprint(user_blueprint)

    return app
