from flask_wtf import FlaskForm
from wtforms.fields.simple import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class RegistrationForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired(), Email()])
    submit = SubmitField("Register")
