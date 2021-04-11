import uuid

from flask_sqlalchemy import SQLAlchemy

"""
Add a SQLAlchemy object for the User object,
and a database engine initialization code.
The User object won't be used by the app in any meaningful way,
but we we use it to make sure database migrations work and SQLAlchemy-Flask integration is set up correctly.
"""


db = SQLAlchemy()


class User(db.Model):
   id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
   username = db.Column(db.String())
   email = db.Column(db.String(), unique=True)