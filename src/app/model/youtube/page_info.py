from dataclasses import dataclass


@dataclass
class PageInfo:
    totalResults: int
    resultsPerPage: int
