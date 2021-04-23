from flask import render_template

from components import app


@app.route('/')
def main_page():
    return render_template('index.html')
