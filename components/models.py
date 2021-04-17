from flask_login import UserMixin
from sqlalchemy import PrimaryKeyConstraint

from components import db


class User(db.Model, UserMixin):
    __tabname__ = 'user'
    __table_args__ = (
        PrimaryKeyConstraint('id'),
    )

    id = db.Column(db.Integer, autoincrement=True, unique=True)
    login = db.Column(db.String, nullable=True, unique=True)
    email = db.Column(db.String, nullable=True, unique=True)
    password = db.Column(db.String, nullable=True)
