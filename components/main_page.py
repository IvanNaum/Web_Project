from flask import render_template
from flask_login import current_user

from components import app


@app.route('/')
def main_page():
    test = current_user

    return render_template('index.html', current_user=current_user)
