import configparser

import googleapiclient.discovery


class YoutubeClient:
    api_service_name = "youtube"
    api_version = "v3"
    youtube_client: googleapiclient.discovery.Resource

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.properties")
        playlist_id: str = config.get("Youtube", "playlist_id")

        self.youtube_client = googleapiclient.discovery.build(
            self.api_service_name,
            self.api_version,
            developerKey=config.get("Google_API", "api_key"))

    def get_playlist_item_count(self, playlist_id: str):
        response: dict = self.youtube_client.playlistItems().list(
            maxResults=0,
            part="contentDetails",
            playlistId=playlist_id
        ).execute()

        total_results = response.get("pageInfo").get("totalResults")
        page_token = response.get("nextPageToken")
        print("Playlist {} has {} elements.".format(playlist_id, total_results))
        return total_results, page_token

    def get_playlist_items(self, playlist_id: str):
        total_results: tuple = self.get_playlist_item_count(playlist_id)
        count = total_results[0]
        total = 0
        page_token = total_results[1]
        video_ids = set()

        while count > total:
            playlist_items_response: dict = self.youtube_client.playlistItems().list(
                pageToken=page_token,
                part="contentDetails",
                maxResults=50,
                playlistId=playlist_id
            ).execute()

            page_token = playlist_items_response.get("nextPageToken")
            total += 50
            items: [] = playlist_items_response.get("items")
            video_ids.update([item.get("contentDetails").get("videoId") for item in items])

        return video_ids
