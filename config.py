import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:sagemovie@localhost/youtube_dashboard'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY') or 'AIzaSyDXIBQqCLe6BgWFq9NV9FURdAY7X941SOw'