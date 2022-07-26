from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class Registration_Form(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=3, max=25)], render_kw={'placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(min = 8, max=20)], render_kw={'placeholder': 'Password'})
    password2 = PasswordField(validators=[InputRequired(), Length(min = 8, max=20), EqualTo('password')], render_kw={'placeholder': 'Confirm Password'})
    email = EmailField(validators=[InputRequired(), Length(max=30)], render_kw={'placeholder': 'Email'})
    submit = SubmitField('Signup')


class Login_Form(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=3, max=25)], render_kw={'placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(min = 8, max=20)], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Login')
