from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class InsertForm(FlaskForm):
    name  = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    message = StringField('message', validators=[DataRequired()])
    date = StringField('message', validators=[DataRequired()])

class DeleteForm(FlaskForm):
    name  = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])





                        
