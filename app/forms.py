from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField , validators
from wtforms.validators import DataRequired 

class LoginForm(FlaskForm):
    vlen5to10 = validators.Length( min=5,max=10)
    username = StringField('Username  : ', validators=[ vlen5to10  , DataRequired(message="*Require!!") \
        ], render_kw={"onclick": "console.log('clicked')","style":"background-color:yellow;"})
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SearchUserByName(FlaskForm):
    vlen5to10 = validators.Length( min=2,max=10)
    username = StringField('Username  : ', validators=[ vlen5to10  , DataRequired(message="*Require!!") \
        ], render_kw={"onclick": "console.log('clicked')","style":"background-color:yellow;"})
    submit = SubmitField('ค้นหา')
