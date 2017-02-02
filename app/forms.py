from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import Length, Email, EqualTo, DataRequired
from wtforms.fields.html5 import EmailField

class RegistrationForm(Form):
    username = StringField(
        'Username',
        [
            Length(min=4,
                   max=25,
                   message="Field must be between 4 and 25 characters long."),
        ]
    )
    email = EmailField(
        'Email Address',
        [
            DataRequired(message="필수 항목입니다"),
            Length(min=6, max=35),
            Email("enter your valid email address.")
        ]
    )
    password = PasswordField('New Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField(
        'I accept the TOS',
        [DataRequired(message="약관에 동의 하셔야 합니다.")]
    )
