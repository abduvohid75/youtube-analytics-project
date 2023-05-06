import json
import os
import pickle
import requests
from googleapiclient.discovery import build
class Video:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.video = self.youtube.videos().list(id=self.video_id, part='snippet, statistics').execute()
        self.title = self.video['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/watch/{self.video['items'][0]['id']}"
        self.view_count = self.video['items'][0]['statistics']['viewCount']
        self.likeCount = self.video['items'][0]['statistics']['likeCount']
class PLVideo(Video):
    def __init__(self, video_id, channel_id):
        super().__init__(video_id)
        self.channel_id = channel_id
        self.channel_id = self.video['items'][0]['snippet']['channelId']

