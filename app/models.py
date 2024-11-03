from app import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    author = db.Column(db.String(100), nullable=False)