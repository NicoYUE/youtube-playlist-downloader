import requests
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

from util.media_utility import mp4_to_mp3, emb_art_to_mp3


class YtDownloader:
    output_path: str

    def __init__(self, output_path: str):
        self.output_path = output_path

    def download_audio(self, video_id: str):
        video_url: str = "https://youtu.be/{}".format(video_id)
        youtube = YouTube(video_url)

        try:
            print("Downloading: " + format( youtube.title))
        except:
            print("Error when trying to get title from " + video_id)

        try:
            stream = youtube.streams.filter(only_audio=True).first()
            video_output_path = stream.download(self.output_path)
            return mp4_to_mp3(video_output_path)
        except VideoUnavailable:
            print("Cannot access id:{}, title is {}".format(video_id,  youtube.title))
            pass

    def download_thumbnail(self, video_id: str):
        thumbnail_url: str = "https://img.youtube.com/vi/{}/maxresdefault.jpg".format(video_id)
        thumbnail = requests.get(thumbnail_url).content
        thumbnail_out_path = self.output_path + video_id

        with open(thumbnail_out_path, "wb") as w:
            w.write(thumbnail)
        return thumbnail_out_path

    def download_audio_with_thumbnail(self, video_id: str):
        audio_output = self.download_audio(video_id)
        if audio_output is not None:
            thumbnail_output = self.download_thumbnail(video_id)
            emb_art_to_mp3(audio_output, thumbnail_output, True)
