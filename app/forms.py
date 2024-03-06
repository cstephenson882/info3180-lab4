
# from flask_wtf import FlaskForm, FileField, FileAllowed, FileRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from wtforms import SubmitField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file = FileField('Upload File', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    # submit = SubmitField('Upload')
    
