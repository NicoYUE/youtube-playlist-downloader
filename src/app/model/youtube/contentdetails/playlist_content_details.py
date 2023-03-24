from dataclasses import dataclass
from model.youtube.contentdetails.content_details import ContentDetails


@dataclass()
class PlaylistContentDetails(ContentDetails):
    videoId: str
    videoPublishedAt: str
