import json
import os
import pickle

import requests
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel['items'][0]['id']}"
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']







    def print_info(self) -> None:
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        self.title = self.channel[1]['snippet']['title']
        self.description = self.channel[0]['snippet']['description']
        print(self.channel)

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, file_name):
        state = {}
        state["title"] = self.title
        state["description"] = self.description
        state["url"] = self.url
        state["subscriber_count"] = self.subscriber_count
        state["video_count"] = self.video_count
        state["view_count"] = self.view_count


        with open(file_name, "wt") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

        return vdud


    def __str__(self):
        return f"{self.title} {self.url}"

    @property
    def __add__(self, other):
        return self.subscriber_count, other.subscriber_count
















