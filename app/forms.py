from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    username = StringField('username', validators = [InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    email = StringField('email', validators = [InputRequired()])
    firstname = StringField('firstname', validators = [InputRequired()])
    lastname = StringField('lastname', validators = [InputRequired()])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField('biography', validators = [InputRequired()])
    profile_photo = FileField('profile_photo', validators = [FileAllowed(['jpg', 'png'], 'Pictures Only!')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    photo = FileField('Photo', validators=[DataRequired()])
    caption = TextAreaField('Caption', validators=[DataRequired()])
    submit = SubmitField('Post')

