from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column()