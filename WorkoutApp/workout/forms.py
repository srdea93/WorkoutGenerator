from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired

class Workout_Form(FlaskForm):
    total_workout_time = SelectField(choices=[5, 10, 15, 20, 25, 30, 45, 60],
                                     validators=DataRequired())
    type_of_workout = SelectField(choices=['Cardio', 'Total Body', 'Abs', 'Arms', 'Legs', 'Butt'])
    # include a 5 minute warmup?
    warm_up = SelectField(choices=['Yes', 'No'], validators=DataRequired())
    submit = SubmitField('Submit')