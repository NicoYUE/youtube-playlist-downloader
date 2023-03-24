from dataclasses import dataclass
from model.youtube.contentdetails.content_details import ContentDetails


@dataclass
class Item:
    kind: str
    etag: str
    id: str
    contentDetails: ContentDetails
