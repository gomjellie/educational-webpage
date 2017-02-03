from wtforms import Form, BooleanField, StringField, PasswordField, IntegerField
from wtforms.validators import Length, Email, EqualTo, DataRequired
from wtforms.fields.html5 import EmailField

class RegistrationForm(Form):
    username = StringField(
        '이름',
        [
            DataRequired(message="필수 항목입니다")
        ]
    )
    student_id = StringField(
        '학번',
        [
            DataRequired(message="필수 항목입니다")
        ]
    )
    email = EmailField(
        '@ssu.ac.kr 계정',
        [
            DataRequired(message="필수 항목입니다"),
            Length(min=3, max=35),
            Email(message="enter your valid email address.")
        ]
    )
    password = PasswordField('비밀번호', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    major = StringField(
        '전공',
        [
            DataRequired(message="필수 항목입니다"),
            Length(min=1, max=16)
        ]
    )

    phone_number = StringField(
        '핸드폰 번호(-제외)',
        [
            DataRequired(message="필수 항목입니다"),
            Length(min=10, max=12)
        ]
    )

    accept_tos = BooleanField(
        '위 약관에 동의합니다',
        [
            DataRequired(message="약관에 동의 하셔야 합니다.")
        ]
    )
