from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import InputRequired, Email, EqualTo, email_validator

class delComment(FlaskForm):
    submit = SubmitField('Delete')

class UserForm(FlaskForm):
    profile_pic = FileField('Profile Picture')

class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[InputRequired()])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[InputRequired()])
    submit = SubmitField('Search')

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    password = PasswordField('Password', validators = [InputRequired()])
    full_name = StringField('Full Name', validators = [InputRequired()])
    email = StringField('Email', validators = [InputRequired()])
    course = StringField('Course', validators = [InputRequired()])
    department = StringField('Department', validators = [InputRequired()])
    hostel = StringField('Hostel', validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators = [InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')