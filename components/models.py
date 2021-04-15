from flask_login import UserMixin
from sqlalchemy import PrimaryKeyConstraint

from components import db, login_manager


class User(db.Model, UserMixin):
    __tabname__ = 'user'
    __table_args__ = (
        PrimaryKeyConstraint('id'),
    )

    id = db.Column(db.Integer, autoincrement=True)
    login = db.Column(db.String)
    password = db.Column(db.String, nullable=True)
