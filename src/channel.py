import json
import os
import pickle

import requests
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY_YOU_TUBE')
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        self.title = self.channel['title']
        self.description = description
        self.url = url
        self.subscriber_count = subscriber_count
        self.video_count = video_count
        self.view_count = view_count

    def print_info(self) -> None:
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        self.title = self.channel[1]['snippet']['title']
        self.description = self.channel[0]['snippet']['description']
        print(self.channel)

    @classmethod
    def get_service(cls):
        return
    def to_json(dict_to_print: dict):
        state = {}
        state["title"] = self.title
        state["description"] = self.description
        state["url"] = self.url
        state["subscriber_count"] = self.subscriber_count
        state["video_count"] = self.video_count
        state["view_count"] = self.view_count

        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
        with open("file.json", "wb") as f:
            pickle.dump(self.state, f)

