from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields.html5 import EmailField
from werkzeug.security import check_password_hash

from app.models import User

data_required = DataRequired('Заполните это поле')
email = Email('Некорректный email')


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[data_required])
    password = PasswordField('Пароль', validators=[data_required])
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[data_required, email])
    login = StringField('Логин', validators=[data_required])
    password = PasswordField('Пароль', validators=[data_required])
    password2 = PasswordField(
        'Повторите пароль', 
        validators=[data_required, EqualTo("password", 'Пароли не совпадают')]
    )
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self):
        if User.query.filter_by(email=self.email.data).first():
            return False
        return True

    def validate_login(self):
        if User.query.filter_by(login=self.login.data).first():
            return False
        return True
