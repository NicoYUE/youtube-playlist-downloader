# file_utility.py
import os

from mutagen.id3 import ID3, APIC
from mutagen.mp3 import MP3


def change_extension(file_path: str, extension: str):
    base = os.path.splitext(file_path)[0]
    renamed_path = base + "." + extension
    os.rename(file_path, renamed_path)


def add_art_to_audio_file(audio_path: str, art_path: str):
    audio = MP3(audio_path, ID3=ID3)
    audio.tags.add(
        APIC(
            encoding=3,
            mime="image/jpeg",
            type=3,
            data=open(art_path).read()
        )
    )


