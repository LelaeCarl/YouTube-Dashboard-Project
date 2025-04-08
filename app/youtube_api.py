# app/youtube_api.py
import requests
from flask import current_app
from datetime import datetime

def fetch_videos_by_keyword(keyword):
    api_key = current_app.config['YOUTUBE_API_KEY']
    search_url = f'https://www.googleapis.com/youtube/v3/search'
    video_url = f'https://www.googleapis.com/youtube/v3/videos'

    search_params = {
        'part': 'snippet',
        'q': keyword,
        'key': api_key,
        'maxResults': 10,
        'type': 'video'
    }

    search_res = requests.get(search_url, params=search_params).json()

    video_ids = [item['id']['videoId'] for item in search_res.get('items', [])]

    video_params = {
        'part': 'snippet,statistics',
        'id': ','.join(video_ids),
        'key': api_key
    }

    video_res = requests.get(video_url, params=video_params).json()
    videos = []

    for item in video_res.get('items', []):
        videos.append({
            'video_id': item['id'],
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'channel_title': item['snippet']['channelTitle'],
            'publish_date': item['snippet']['publishedAt'],
            'views': int(item['statistics'].get('viewCount', 0)),
            'likes': int(item['statistics'].get('likeCount', 0)),
            'comments': int(item['statistics'].get('commentCount', 0)),
            'tags': ','.join(item['snippet'].get('tags', [])),
            'thumbnail_url': item['snippet']['thumbnails']['high']['url']
        })

    return videos
