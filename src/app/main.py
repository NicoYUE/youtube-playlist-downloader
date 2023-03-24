import configparser

from cache.id_cache import IdCache
from client.youtube_client import YoutubeClient
from yt.yt_downloader import YtDownloader

if __name__ == '__main__':

    # TODO: create an interface to fill those informations rather than rely on a config file
    config = configparser.ConfigParser()
    config.read("config.properties")
    playlist_id: str = config.get("Youtube", "playlist_id")
    output_path: str = config.get("Directory", "output_path")

    id_cache = IdCache("id_cache.txt")
    id_cache.load_values()

    # PyTube's playList is inaccurate, rather rely on Data API to retrieve IDs
    videos_ids: set = YoutubeClient().get_playlist_items(playlist_id)

    for video_id in videos_ids:
        if id_cache.exists(video_id):
            print("Skipping Video {}  : It has already been downloaded".format(video_id))
            continue

        YtDownloader(output_path).download_audio_with_thumbnail(video_id)

        id_cache.set(video_id)
