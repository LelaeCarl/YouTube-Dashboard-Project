# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.youtube_api import fetch_videos_by_keyword
from app.models import Video
from app import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    videos = fetch_videos_by_keyword(keyword)

    for video in videos:
        if not Video.query.filter_by(video_id=video['video_id']).first():
            new_video = Video(
                video_id=video['video_id'],
                title=video['title'],
                description=video['description'],
                channel_title=video['channel_title'],
                publish_date=datetime.strptime(video['publish_date'], "%Y-%m-%dT%H:%M:%SZ"),
                views=video['views'],
                likes=video['likes'],
                comments=video['comments'],
                tags=video['tags'],
                thumbnail_url=video['thumbnail_url']
            )
            db.session.add(new_video)
    db.session.commit()

    return render_template('channel.html', videos=videos)

@main.route('/analytics')
def analytics():
    videos = Video.query.order_by(Video.views.desc()).limit(10).all()
    top_tags = {}
    for video in videos:
        if video.tags:
            for tag in video.tags.split(','):
                top_tags[tag] = top_tags.get(tag, 0) + 1

    return render_template('analytics.html', videos=videos, tags=top_tags)
