from flask import request, render_template, flash, redirect
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from components import app, db, login_manager
from components.models import User


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        login, password = request.form.get('login'), request.form.get('password')

        if login and password:
            user = User.query.filter_by(login=login).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect('/')
                else:
                    flash('Пароль или логин некорректен')
            else:
                flash('Пароль или логин некорректен')
        else:
            flash('Заполните все поля')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        login = request.form.get('login')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not all((login, email, password1, password2)):
            flash('Заполните все обязательные поля')
        elif password1 != password2:
            flash('Пароли не совпадают')
        else:
            hash_password = generate_password_hash(password1)
            user = User(login=login, password=hash_password, email=email)
            db.session.add(user)
            db.session.commit()

            return redirect('/login')

    return render_template('register.html')


@app.route('/logout', methods=['GET'])
@login_required
def logout_page():
    logout_user()
    return redirect('/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
