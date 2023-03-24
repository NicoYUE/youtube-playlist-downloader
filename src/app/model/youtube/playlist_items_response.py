from dataclasses import dataclass
from typing import List

from model.youtube.item import Item
from model.youtube.page_info import PageInfo


@dataclass
class PlaylistItemsResponse:
    kind: str
    etag: str
    nextPageToken: str
    items: List[Item]
    pageInfo: PageInfo

