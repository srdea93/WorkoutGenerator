from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired

class Exercise_Form(FlaskForm):
    exercise_name = StringField('Exercise', validators=DataRequired())
    # same as type of workout
    exercise_type = SelectField(choices=['Cardio', 'Total Body', 'Abs', 'Arms', 'Legs', 'Butt'],
                                validators=DataRequired())
    # time is in minutes
    recommended_time = SelectField(choices=[1, 1.5, 2, 2.5, 5], validators=DataRequired())

    demonstration_link = StringField('Link', validators=None)

    submit = SubmitField('Submit')


