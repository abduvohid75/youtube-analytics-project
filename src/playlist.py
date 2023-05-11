import datetime
import json
import os
import pickle
import requests
from googleapiclient.discovery import build


class Playlist:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_videos_id: str) -> None:
        self.playlist_videos_id = playlist_videos_id
        #        print(self.playlist_videos_id)
        self.playlist_videos = self.youtube.playlists().list(id=self.playlist_videos_id, part='snippet',
                                                             maxResults=50).execute()
        # print(self.playlist_videos)
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_videos['items'][0]['id']}"
        self.title = self.playlist_videos['items'][0]['snippet']['title']

    def total_duration(self):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_videos_id, part='contentDetails',
                                                       maxResults=50).execute()
        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails, statistics', id=','.join(video_ids)).execute()

        len_min = 0
        len_sec = 0
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            len_min += int(iso_8601_duration[2] + iso_8601_duration[3])
            len_sec += int(iso_8601_duration[5] + iso_8601_duration[6])

        x = int(len_sec / 60)
        len_min += x
        len_sec = len_sec - x * 60
        len_hours = int(len_min / 60)
        len_min = len_min - len_hours * 60

        total_video_duration = datetime.timedelta(hours=len_hours, minutes=len_min, seconds=len_sec)

        return total_video_duration

    def show_best_video(self):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_videos_id, part='contentDetails',
                                                       maxResults=50).execute()
        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails, statistics', id=','.join(video_ids)).execute()
        best_video_like_count = 0
        best_video_url = ''
        #      print(playlist_videos)
        for video in video_response['items']:

            like_count = int(video['statistics']['likeCount'])

            if like_count > best_video_like_count:
                best_video_like_count = like_count
                best_video_url = f"https://youtu.be/{video['id']}"

        return best_video_url
