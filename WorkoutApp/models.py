from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from WorkoutApp import db, login_manager


class User(db.Model, UserMixin):
    pass


class Workout(db.Model):
    pass


class Exercise(db.Model):
    pass

