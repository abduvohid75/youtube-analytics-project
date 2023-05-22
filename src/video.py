import json
import os
import pickle
import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
class Video:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.video = self.youtube.videos().list(id=self.video_id, part='snippet, statistics').execute()
        try:
            self.title = self.video['items'][0]['snippet']['title']
        except IndexError:
            self.title = None
            print(1)

        try:
            self.url = f"https://www.youtube.com/watch/{self.video['items'][0]['id']}"
        except IndexError:
            print(2)
        try:
            self.view_count = self.video['items'][0]['statistics']['viewCount']
        except:
            self.view_count = None
            print(3)
        try:
            self.likeCount = self.video['items'][0]['statistics']['likeCount']
        except:
            self.likeCount = None
            print(4)

class PLVideo(Video):
    def __init__(self, video_id, channel_id):
        super().__init__(video_id)
        self.channel_id = self.video['items'][0]['snippet']['channelId']

