import json
import os
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

    def print_info(self) -> None:
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        print(channel_id)

    @classmethod
    def get_service(cls):
        return
    def to_json(dict_to_print: dict) -> None:
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

