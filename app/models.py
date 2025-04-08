# app/models.py
from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    channel_title = db.Column(db.String(255))
    publish_date = db.Column(db.DateTime)
    views = db.Column(db.Integer)
    likes = db.Column(db.Integer)
    comments = db.Column(db.Integer)
    tags = db.Column(db.Text)
    thumbnail_url = db.Column(db.String(255))
