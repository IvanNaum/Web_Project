from flask import request, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from app import app, db, login_manager
from app.models import User
from app.forms import LoginForm, RegisterForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        login, password = request.form.get('login'), request.form.get('password')

        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Пароль или логин некорректен')

    return render_template('login.html', form=form, title='Вход')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        login = form.login.data
        email = form.email.data
        password = form.password.data

        if not form.check_email():
            flash('Этот email уже занят')
        elif not form.check_login():
            flash('Этот логин уже занят')
        else:
            hash_password = generate_password_hash(password)
            user = User(login=login, password=hash_password, email=email)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('login'))

    return render_template('register.html', form=form, title='Регистрация')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
