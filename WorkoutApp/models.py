from flask_login import UserMixin
from WorkoutApp import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Need to create a custom sqlalchemy column for this? or create a separate text file?
    exercise_dict = db.Column
    exercise_time = db.Column(db.Integer, nullable=False)


class Exercise(db.Model):
    name = db.Column(db.String, primary_key=True)

